import sys
import subprocess
#script for cloudformation templates


# NOTE: i made this on python just to challange myself and get a hang of python,
#   i included solution.sh which is from a previous exersie just in case this didnt work,it follows the same parameters.

# Parameters
#  sys.argv[1] is the execution mode with only 3 valid values: deploy, delete, preview.
#  sys.argv[2] is the desired region.
#  sys.argv[3] the name of the cloudformation stack.
#  sys.argv[4] our template file
#  sys.argv[5] our parameters file.

#Usage example, ran through bash:
#   python run.py deploy us-east-1 udaDemo udagram.yml udagram-parameters.json
#   python run.py preview us-east-1 udaDemo udagram.yml udagram-parameters.json
#   python run.py delete us-east-1 udaDemo
def main():
    # Validate parameters
    valid_modes = ["deploy", "delete", "preview"]
    if sys.argv[1] not in valid_modes:
        print("ERROR: Incorrect execution mode. Valid values: deploy, delete, preview.")
        sys.exit(1)
    

    EXECUTION_MODE = sys.argv[1]

    # REGION = sys.argv[2]
    # STACK_NAME = sys.argv[3]
    # TEMPLATE_FILE_NAME = sys.argv[4]
    # PARAMETERS_FILE_NAME = sys.argv[5]

    # Execute CloudFormation CLI
    if EXECUTION_MODE == "deploy":

        subprocess.run(["aws", "cloudformation", "deploy",
                        "--stack-name", sys.argv[3],
                        "--template-file", sys.argv[4],
                        "--parameter-overrides", f"file://{sys.argv[5]}",
                        "--capabilities", "CAPABILITY_NAMED_IAM",
                        "--region", sys.argv[2]], check=True)
        
    elif EXECUTION_MODE == "delete":
        subprocess.run(["aws", "cloudformation", "delete-stack",
                        "--stack-name", sys.argv[3],
                        "--region", sys.argv[2]], check=True)
        print(sys.argv[3] +" deleted succesfully")
    elif EXECUTION_MODE == "preview":
        subprocess.run(["aws", "cloudformation", "deploy",
                        "--stack-name", sys.argv[3],
                        "--template-file", sys.argv[4],
                        "--parameter-overrides", f"file://{sys.argv[5]}",
                        "--capabilities", "CAPABILITY_NAMED_IAM",
                        "--no-execute-changeset",
                        "--region", sys.argv[2]], check=True)

if __name__ == "__main__":
    main()