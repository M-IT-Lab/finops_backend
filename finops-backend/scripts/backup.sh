#!/bin/bash
BACKUP_DIR="/home/maikyalmonte120/backups"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# 1. Erstelle den SQL-Dump aller Datenbanken
mysqldump --all-databases > "$BACKUP_DIR/dump_$TIMESTAMP.sql"

# 2. Lösche Dumps, die älter als 7 Tage sind
find "$BACKUP_DIR" -type f -name "dump_*.sql" -mtime +7 -delete
