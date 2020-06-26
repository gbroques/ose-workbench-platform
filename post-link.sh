#!/bin/sh
# ----------------------------------------------------------------------------------
# Executed after the package is installed.
# An error is indicated by a nonzero exist and causes installation to fail.
# If there is an error, conda does not write any package metadata.
#
# By adding the $CONDA_PREFIX/lib directory to $PYTHONPATH, python is able to find
# FreeCAD, FreeCADGui, and other various FreeCAD-related modules during execution.
# 
# See Also:
#   https://docs.conda.io/projects/conda-build/en/latest/resources/link-scripts.html
# ----------------------------------------------------------------------------------
cd $CONDA_PREFIX
mkdir -p ./etc/conda/activate.d
mkdir -p ./etc/conda/deactivate.d
touch ./etc/conda/activate.d/env_vars.sh
touch ./etc/conda/deactivate.d/env_vars.sh

echo '#!/bin/sh' >> ./etc/conda/activate.d/env_vars.sh
echo 'export INITIAL_PYTHONPATH=${PYTHONPATH}' >> ./etc/conda/activate.d/env_vars.sh
echo "export PYTHONPATH=$CONDA_PREFIX/lib:\${PYTHONPATH}" >> ./etc/conda/activate.d/env_vars.sh

echo '#!/bin/sh' >> ./etc/conda/deactivate.d/env_vars.sh
echo 'export PYTHONPATH=${INITIAL_PYTHONPATH}' >> ./etc/conda/deactivate.d/env_vars.sh
echo 'unset INITIAL_PYTHONPATH' >> ./etc/conda/deactivate.d/env_vars.sh
