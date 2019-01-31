# How to install the modified tor client

1. Go to your local repo `shadow-plugin-tor`
2. Delete folder `build/tor` and archive `tor-0.X.Y.Z.tar.gz`.
3. Check which commit are you on (you can use `git show`). If differs from https://github.com/shadow/shadow-plugin-tor/commit/67e966692f55aae739fe4cc7b30334bf133615c9 , checkout this commit (`git checkout 67e9666`).
4. Copy the modified `setup` file from this directory to `shadow-plugin-tor`
5. Run `./setup build` and `./setup install`. 

