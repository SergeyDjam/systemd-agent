# systemd-agent
Агент управляющий сервисами systemd через сеть

Установка:
1. Клонируем репозиторий

```git clone https://github.com/SergeyDjam/systemd-agent.git```

2. Переходим в папку с полученным репозиторием

```cd systemd-agent```

3. Создаем пользователя "systemd-agent"

```sudo useradd systemd-agent```

4. Копируем systemd-agent.sudoers в папку /etc/sudoers.d и переименовываем в systemd-agent

```sudo cp systemd-agent.sudoers /etc/sudoers.d/systemd-agent```

5. Копируем systemd-agent.service в /lib/systemd/system

```sudo cp systemd-agent.service /lib/systemd/system```

6. Копируем systemd-agent.cfg.sample в /etc/ и переименовываем в systemd-agent.cfg

```sudo cp systed-agent.cfg.sample /etc/systemd-agent.cfg```

```sudo vi /etc/systemd-agent.cfg```

Использование:

Запуск агента: 
1. Как отдельное приложение 

выполняем в папке с программой ```./systemd-agent```

2. Как сервис

```sudo systemctl start systemd-agent```

Пример команды перезапуска сервиса

```echo "restart" | nc 127.0.0.1 44044```

