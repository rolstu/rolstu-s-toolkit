
# Label Replacer: Because Life is Meaningless and So Are Your Labels

Welcome to the **Label Replacer**. It’s not going to save the world, but it will replace some numbers in your `.txt` files. Specifically, it replaces the first number of every line. That's it. That's all this script does. Your labels were boring, so we made them... slightly less boring. You're welcome.

## Why?

Honestly, I don't know. Maybe you're stuck on a project that requires labels in your YOLO `.txt` files to be changed. Maybe you're just procrastinating on something more important. Either way, here's a script that swaps `0` with `1` and `1` with `4` — because why not?

## Installation

1. Download the script. Clone it, or don’t. Your choice. The world won't care either way.

   ```bash
   git clone https://github.com/rolstu/rolstu-s-toolkit.git
   cd "Rename Dataset (yolo)"
   ```

2. You probably already have Python 3.x installed. If not, install it. Or stare into the void of your terminal for a while. Both are equally fulfilling.

3. You won’t even need any fancy packages. Just vanilla Python to run this piece of code. The bare minimum, much like your enthusiasm right now.

## Usage

- Specify your **source folder** and **destination folder** in the code. Don't worry about creating the destination folder yourself. The script will do it for you, because even it knows you don’t want to.
  
- Now run it, ugh:

   ```bash
   python renaming_txt_dataset.py
   ```

- Then just sit there, watching numbers change. If that doesn't fill the void in your soul, I don't know what will.

### Example:

Before (a.k.a. your miserable labels):

```
0 0.14765625 0.1609375 0.2953125 0.2125
1 0.57421875 0.2171875 0.4109375 0.2265625
```

After (still miserable, just different):

```
1 0.14765625 0.1609375 0.2953125 0.2125
4 0.57421875 0.2171875 0.4109375 0.2265625
```

The script saves the modified files in the `swap/folder/labels/` directory, as if it’s doing you a huge favor.

## File Structure

Here's how this monument to productivity looks:

```bash
rolstu-s-toolkit/
│
├── Rename Dataset (yolo)/
│   ├── folder/labels/               # Your sad little text files go here
│   ├── swap/folder/labels/          # Your marginally less sad text files come out here
│   └── renaming_txt_dataset.py      # The magic happens here (not really, it’s just some loops)
```

## Contributing

Why would you want to contribute to this? But if you really feel the urge to push some new feature, go ahead:

1. Fork the repo.
2. Do whatever you want. It’s your life.
3. Submit a PR. Or don’t. I’m not your boss.

## License

This project is licensed under the MIT License. That means you can do whatever you want with it. Like literally, I don't care.

---

If changing numbers in text files doesn’t fulfill you, I suggest staring into the abyss. It’s cheaper than therapy.
