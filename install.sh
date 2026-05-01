#!/bin/bash
# INSTALADOR OFICIAL PROYECTO INTERSTELLAR - SAN LUIS GONZAGA

VERDE='\033[1;32m'
NC='\033[0m' # No Color

echo -e "${VERDE}"
echo "-------------------------------------------------------"
echo "   INICIANDO INSTALACIÓN: PROYECTO INTERSTELLAR        "
echo "   COLEGIO DE SAN LUIS GONZAGA                         "
echo "-------------------------------------------------------"
echo -e "${NC}"

# Detectar el sistema operativo
echo ">>> Verificando entorno..."
sleep 1

# Instalar dependencias básicas
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    sudo apt-get update
    sudo apt-get install -y python3 git
elif [[ "$OSTYPE" == "darwin"* ]]; then
    # Para Mac
    brew install python
fi

# Clonar el proyecto de GitHub
echo ">>> Descargando archivos de la nube..."
git clone https://github.com/TU_USUARIO/Interstellar-CSLG.git ~/Interstellar
cd ~/Interstellar

echo -e "${VERDE}"
echo "-------------------------------------------------------"
echo "   INSTALACIÓN FINALIZADA CON ÉXITO                    "
echo "   Para ejecutar: python3 main.py                      "
echo "-------------------------------------------------------"
echo -e "${NC}"
