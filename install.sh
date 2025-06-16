#!/bin/bash
chmod +x crist_starlink.py
cp crist_starlink.py /usr/local/bin/crist-starlink 2>/dev/null || cp crist_starlink.py $PREFIX/bin/crist-starlink
echo "✅ Instalación completada. Ejecuta con: crist-starlink"
