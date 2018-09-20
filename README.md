# simple-discovery
Simple discovery for my rPI

Enable lingering for `pi`

```bash
sudo loginctl enable-linger pi
```
Prepare the service:

```bash
mkdir -p ~/.config/systemd/user/
cp discovery-listener.service ~/.config/systemd/user/
```

Start the service:
```bash
systemctl --user enable discovery-listener
```

