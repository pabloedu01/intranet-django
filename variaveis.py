import os

# Nome do arquivo .env
env_file = ".env"

# Nome do arquivo .env-example
env_example_file = ".env-example"

# Lê as variáveis do arquivo .env
with open(env_file, "r") as f:
    env_vars = f.readlines()

# Cria o arquivo .env-example
with open(env_example_file, "w") as f:
    for env_var in env_vars:
        env_var = env_var.strip()
        if "=" not in env_var:
            continue
        env_var_name, env_var_value = env_var.split("=")
        if env_var_value:
            f.write(f"{env_var_name}=\n")
        else:
            f.write(f"{env_var_name}={env_var_value}\n")
