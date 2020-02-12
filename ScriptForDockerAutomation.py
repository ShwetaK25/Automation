"""
Auther: Shweta Katkade.
This script does some processes related to docker automatically
"""

import os
import subprocess
import logging
import argparse


def validate_path_in_command_line_option(input_path, default_path=None):
    """
    Validates a path provided in a command-line option. It will transform
    an argument to an absolute path.

    :param input_path: Input path provided in the command-line
    :param default_path: In input_path is None, use returns a default_path
    :return:
    """
    if input_path:
        if not os.path.isabs(input_path):
            input_path = os.path.join(os.getcwd(), *(input_path.split(os.sep)))
        if not os.path.isdir(os.path.dirname(input_path)):
            os.makedirs(os.path.dirname(input_path))
    else:
        input_path = default_path
    return input_path



def docker_things(args):
    """
    Compilation for Linux
    """
    # Make sure the docker container is running to retrieve running container id
    docker_info = subprocess.check_output('docker ps', shell=True)
    docker_info_list = docker_info.decode().split(" ")
    count = 0
    container_id = ''
    for i in docker_info_list:
        if "NAMES" in i:
            container_id = i.replace("NAMES\n", '')
            count = count + 1

    if count == 0:
        # Start docker container if it's not running and retrieve running container id
        
        subprocess.Popen('docker run -i abc/runtime_demo:2019.3 bash', shell=True)
        docker_info = subprocess.check_output('docker ps', shell=True)
        docker_info_list = docker_info.decode().split(" ")
        for i in docker_info_list:
            if "NAMES" in i:
                container_id = i.replace("NAMES\n", '')


    # Copy files from windows to docker & docker to windows and run compilation
    cur_path = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
    model_log1 = os.path.join(cur_path, "log_linux.txt")
    compiler = os.path.join(cur_path, "compile")
    return_code1 = ''
    if args.mofilelib == "Non-ASL":
        return_code1 = subprocess.call(
            "docker cp " + compiler + " " + container_id + ":/compilation && docker cp \"" + mo_file + "\" "
            + container_id + ":/compilation && docker cp " + dmo_file + " " +
            container_id + ":/compilation && docker exec " + container_id +
            " /compilation/compile /compilation/" + mo_filename1 +
            " --outputfile /compilation/" + dmo_filename1 + 
            args.modelname + " /compilation/" + dmo_filename1
            + " --logfile /compilation/_log_linux.txt && docker cp "
            + container_id + ":/compilation/log_linux.txt " + output_dir+" && docker cp "
            + container_id + ":/compilation/" + dmo_filename1 + " " + output_dir, shell=True)
   
    #check subprocess passes or failed
    if return_code1 == 0:
        print("Model for Linux created at "+output_dir)
        return os.path.join(output_dir, dmo_filename1)
    else:
        logging.error('Compilation for Linux failed. See "{}" for details'.format(model_log1))
        return None


if __name__ == '__main__':
    # Compilation flow starts here
    parser = argparse.ArgumentParser()
    parser.add_argument('--outputdir',    type=str,  help='Directory to save the file')
    args = parser.parse_args()
    docker_things(args)
