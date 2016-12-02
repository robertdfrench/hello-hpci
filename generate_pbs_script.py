import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--account')
parser.add_argument('--walltime')
parser.add_argument('--num_nodes')
parser.add_argument('--deployment_root')
parser.add_argument('--num_ranks')
parser.add_argument('--executable_filename')
args = parser.parse_args()

with open('hello_world.template.pbs') as f:
    template = f.read()

pbs_script = template.format(
        account=args.account, walltime=args.walltime, num_nodes=args.num_nodes,
        deployment_root=args.deployment_root, num_ranks=args.num_ranks,
        executable_filename=args.executable_filename)

print(pbs_script)
