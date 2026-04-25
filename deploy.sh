#!/bin/bash
# ============================================================
# Ryventis Solutions — Deploy a producción con un comando
# Flujo: Local (SSD) → GitHub (Private Repo) → Hostinger (Webhook)
#
# USO:
#   bash deploy.sh                    # commit con timestamp automático
#   bash deploy.sh "Descripción"      # commit con mensaje personalizado
#
# SETUP INICIAL (solo una vez):
#   1. git init                                (si el repo no existe aún)
#   2. git remote add origin git@github.com:TU_USUARIO/ryventis-web.git
#   3. En Hostinger Panel → Advanced → Git → conectar repo → branch: main
#   4. Copiar el webhook URL de Hostinger → pegarlo en GitHub:
#      Repo → Settings → Webhooks → Add webhook → Content-Type: application/json
#
# REQUISITOS:
#   - Git instalado y configurado con tu usuario/email
#   - SSH key configurada en GitHub (git@github.com funciona)
#   - Hostinger con Git Deployment habilitado apuntando a branch: main
# ============================================================

set -e  # Detener si cualquier comando falla

# ---- Colores para output ----
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # Sin color

echo -e "${CYAN}============================================${NC}"
echo -e "${CYAN}  Ryventis Solutions — Deploy a Producción${NC}"
echo -e "${CYAN}============================================${NC}"
echo ""

# ---- Verificar que estamos en un repo git ----
if ! git rev-parse --git-dir > /dev/null 2>&1; then
  echo -e "${RED}✗ Error: No estás en un repositorio git.${NC}"
  echo -e "  Ejecuta: git init && git remote add origin git@github.com:TU_USUARIO/ryventis-web.git"
  exit 1
fi

# ---- Mensaje del commit ----
TIMESTAMP=$(date '+%Y-%m-%d %H:%M')
MSG=${1:-"deploy: $TIMESTAMP"}

# ---- Verificar si hay cambios ----
if git diff --quiet && git diff --staged --quiet && [ -z "$(git ls-files --others --exclude-standard)" ]; then
  echo -e "${YELLOW}⚠ No hay cambios para deployar.${NC}"
  echo -e "  El sitio en producción ya está actualizado."
  exit 0
fi

# ---- Mostrar archivos a commitear ----
echo -e "${YELLOW}Archivos modificados:${NC}"
git status --short
echo ""

# ---- Stage todos los cambios ----
echo -e "${CYAN}[1/3] Staging cambios...${NC}"
git add -A
echo -e "${GREEN}✓ Cambios staged${NC}"

# ---- Commit ----
echo -e "${CYAN}[2/3] Commiteando: \"${MSG}\"${NC}"
git commit -m "$MSG"
echo -e "${GREEN}✓ Commit creado${NC}"

# ---- Push a GitHub → dispara webhook Hostinger ----
echo -e "${CYAN}[3/3] Push a GitHub (origin/main)...${NC}"
git push origin main
echo -e "${GREEN}✓ Push completado${NC}"

echo ""
echo -e "${GREEN}============================================${NC}"
echo -e "${GREEN}  ✅ Deploy completado exitosamente${NC}"
echo -e "${GREEN}============================================${NC}"
echo -e "  🌐 URL: ${CYAN}https://ryventis.mx${NC}"
echo -e "  📡 Hostinger recibe el webhook automáticamente"
echo -e "  ⏱  El sitio se actualiza en ~30 segundos"
echo ""
echo -e "  Commit: ${YELLOW}$(git log -1 --format='%h %s')${NC}"
