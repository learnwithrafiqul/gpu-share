import GPUtil

# Get the list of available GPUs
gpus = GPUtil.getGPUs()

if not gpus:
    print("No GPU found.")
else:
    for i, gpu in enumerate(gpus):
        print(f"GPU {i + 1}:")
        print(f"  ID: {gpu.id}")
        print(f"  Name: {gpu.name}")
        print(f"  Driver: {gpu.driver}")
        print(f"  GPU Memory Total: {gpu.memoryTotal} MB")
        print(f"  GPU Memory Free: {gpu.memoryFree} MB")
        print(f"  GPU Memory Used: {gpu.memoryUsed} MB")
        print(f"  GPU Load: {gpu.load * 100}%")
        print(f"  GPU Temperature: {gpu.temperature} °C")
        print()

# You can access more information about the GPU by exploring the 'gpu' object
# For example, gpu.id, gpu.name, gpu.driver, gpu.memoryTotal, etc.
