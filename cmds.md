# Crear un venv para scripts
python3.9 -m venv venv

# Activación de ambiente virtual
source venv/bin/activate

# Instalación de dependencias
pip install -r requirements.txt

# Abrir jupyter notebook
jupyter notebook

# Ejecutar script
python cap_01/scripts/hola_mundo.py