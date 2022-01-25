from prefect import flow

@flow
def hello_world(name="world"):
    print(f"Hello, {name}")

from prefect.deployments import DeploymentSpec

DeploymentSpec(
    flow=hello_world,
    name="my-python-deployment",
    parameters={"name": "Earth"},
    tags=["foo", "bar"],
)

# hello_world()