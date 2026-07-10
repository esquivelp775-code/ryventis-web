#!/bin/bash
# ============================================================
# Ryventis Solutions â€” Deploy a producciÃ³n con un comando
# Flujo: Local (SSD) â†’ GitHub (Private Repo) â†’ Hostinger (Webhook)
#
# USO:
#   bash deploy.sh                    # commit con timestamp automÃ¡tico
#   bash deploy.sh "DescripciÃ³n"      # commit con mensaje personalizado
#
# SETUP INICIAL (solo una vez):
#   1. git init                                (si el repo no existe aÃºn)
#   2. git remote add origin git@github.com:TU_USUARIO/ryventis-web.git
#   3. En Hostinger Panel â†’ Advanced â†’ Git â†’ conectar repo â†’ branch: main
#   4. Copiar el webhook URL de Hostinger â†’ pegarlo en GitHub:
#      Repo â†’ Settings â†’ Webhooks â†’ Add webhook â†’ Content-Type: application/json
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
echo -e "${CYAN}  Ryventis Solutions â€” Deploy a ProducciÃ³n${NC}"
echo -e "${CYAN}============================================${NC}"
echo ""

# ---- Verificar que estamos en un repo git ----
if ! git rev-parse --git-dir > /dev/null 2>&1; then
  echo -e "${RED}âœ— Error: No estÃ¡s en un repositorio git.${NC}"
  echo -e "  Ejecuta: git init && git remote add origin git@github.com:TU_USUARIO/ryventis-web.git"
  exit 1
fi

# ---- Mensaje del commit ----
TIMESTAMP=$(date '+%Y-%m-%d %H:%M')
MSG=${1:-"deploy: $TIMESTAMP"}

# ---- Verificar si hay cambios ----
if git diff --quiet && git diff --staged --quiet && [ -z "$(git ls-files --others --exclude-standard)" ]; then
  echo -e "${YELLOW}âš  No hay cambios para deployar.${NC}"
  echo -e "  El sitio en producciÃ³n ya estÃ¡ actualizado."
  exit 0
fi

# ---- Mostrar archivos a commitear ----
echo -e "${YELLOW}Archivos modificados:${NC}"
git status --short
echo ""

# ---- Stage archivos del sitio web ----
echo -e "${CYAN}[1/3] Staging cambios...${NC}"
git add index.html servicios.html como-funciona.html nosotros.html contacto.html assets/ deploy.sh .gitignore
echo -e "${GREEN}âœ“ Cambios staged${NC}"

# ---- Commit ----
echo -e "${CYAN}[2/3] Commiteando: \"${MSG}\"${NC}"
git commit -m "$MSG"
echo -e "${GREEN}âœ“ Commit creado${NC}"

# ---- Push a GitHub â†’ dispara webhook Hostinger ----
echo -e "${CYAN}[3/3] Push a GitHub (origin/main)...${NC}"
git push origin main
echo -e "${GREEN}âœ“ Push completado${NC}"

echo ""
echo -e "${GREEN}============================================${NC}"
echo -e "${GREEN}  âœ… Deploy completado exitosamente${NC}"
echo -e "${GREEN}============================================${NC}"
echo -e "  ðŸŒ URL: ${CYAN}https://ryventis.com${NC}"
echo -e "  ðŸ“¡ Hostinger recibe el webhook automÃ¡ticamente"
echo -e "  â±  El sitio se actualiza en ~30 segundos"
echo ""
echo -e "  Commit: ${YELLOW}$(git log -1 --format='%h %s')${NC}"
