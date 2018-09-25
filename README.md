# simple-discovery
Simple discovery for my rPI

Enable lingering for `pi`

```bash
sudo loginctl enable-linger pi
```
Prepare the service:

```bash
mkdir -p ~/.config/systemd/user/
ln -t ~/.config/systemd/user/ -s $PWD/discovery-listener.service
```

Start the service:
```bash
systemctl --user enable discovery-listener
```

