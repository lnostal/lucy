## Конфигурация systemd service

ubuntu 22.04

```
pip install aiogram 
pip install peewee --break-system-packages
pip install pymysql
```

```bash
sudo nano /lib/systemd/system/lucy.service
```
Содержание файла:
```
[Unit]
Description=Lucy

[Service]
Type=simple
Restart=always
RestartSec=5s
ExecStart=/usr/bin/python3 /root/lucy/main.py

[Install]
WantedBy=multi-user.target
```

 * перезапуск сервиса и проверка, что все идет хорошо

 ```bash
systemctl daemon-reload
sudo service lucy start
sudo service lucy status
 ```
