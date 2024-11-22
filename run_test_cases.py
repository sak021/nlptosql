import sys
sys.path.append('app/')
from app import cli_app


output = cli_app()
print(output)
