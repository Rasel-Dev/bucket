<h1 align="center">
<img src="https://i.ibb.co/Wpwb3sR/logo.jpg" alt="logo" border="5" width="300" style="border-radius: 5%;">
</h1>

**Bucket are backups of your everyday `Code Templates` and your specific `clipboard data` That are maintained by `Bucket Cli Tool`.
You can restore your backup to your `projects location`. You can restore your backup wherever you want.**

```bash
git clone https://github.com/Rasel-Dev/bucket
cd bucket
```
<p>You must Have <code>pip</code> on your device</p>

```bash
python3 setup.py
```

<p>After Complete Setup The bucket type this <code>bucket -h</code></p>

<pre><b>Usage: bucket [options]

Options:
  -d                    Delete the unnecessary Data !
  -g                    Grab The data from your bucket
  -L                    list of Bucket Directory
  --title               Set The Title for clip content
  --push                push Data into your bucket
  -c, --clone           set the Template for Push
  -l, --list            show list of files in your bucket
  -h, --help            show this help message and exit
</b></pre>

<h2 align="center">Example</h2>

- ### ```How to Push Clip```
```bash
bucket --push clip --title <name>
```
- ### ```How to Grab Clip```
```bash
bucket -g clip --title <name>
```
- ### ```How to Delete Clip```
```bash
bucket -d clip --title <name>
```
- ### ```How to Push Templates```
```bash
bucket --push templates --clone <name>
```
```
bucket --push templates -c <name>
```
- ### ```How to Grab Templates```
```bash
bucket -g template <name>
```
- ### ```How to Delete Templates```
```bash
bucket -d template <name>
```
```bash
bucket -d clip <name>
```