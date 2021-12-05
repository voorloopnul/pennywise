# Pennywise

Pennywise has the ability to shapeshift into the bioinformatic tool you are most afraid to install.

## Requirements

You must have docker and python3 available at your system.

## Install

    pip install pennywise 

## Usage

### List available tools

    pennywise list 

### Basic usage

    pennywise <tool> <regular-tool-options> 

### Example 1: Running trimmomatic

    pennywise trimmomatic PE r1.fq r2.fq r1_p.fq r1_u.fq r2_p.fq r2_u.fq SLIDINGWINDOW:4:20 MINLEN:100

### Example 2: Running spades

```shell
pennywise spades -1 r1_p.fq -2 r2_p.fq -o assembly -meta 
```
    
### First time using a tool

If it's the first time you are running a particular command, pennywise will need to pull the image before it actually 
runs the tool. Most images will range from 200MB to 2GB, and will get installed in less than 10 minutes providing you
have a good internet connection.

```shell
pascal@dione:~/Sandbox/$ pennywise quast genome.fa
- It looks like it's your first time running this command!
- pennywise will download the image (staphb/quast:latest) so it can shapeshift
- This can take some time...
```

## Adding your own tools

 1. Fork this repository
 2. Update pennywise.toml
 3. Run `pennywise source <your-github-user>`

Pennywise will download pennywise.toml from your fork and use it for command reference.

### pennywise.toml format

    [quast]
    image = "staphb/quast:latest"
    prefix_cmd = "quast.py"
    
    [prokka]
    image = "staphb/prokka:latest"
    prefix_cmd = "prokka"

### I don't want to use github as source

It's fine, just update ~/.pennywise/pennywise.toml.

## Tools Available

 - FastANI
 - Prokka
 - Quast
 - Spades
 - Trimmomatic