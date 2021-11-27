# Pennywise

Pennywise has the ability to shapeshift into the bioinformatic tool you are most afraid to install.

## Requirements

You must have docker and python3 available at your system.

## Install

    pip install pennywise 

## Usage

### Basic usage

    pennywise <tool> <regular-tool-options> 

### Running trimmomatic

    pennywise trimmomatic PE r1.fq r2.fq r1_p.fq r1_u.fq r2_p.fq r2_u.fq SLIDINGWINDOW:4:20 MINLEN:100

### Running spades

    pennywise spades -1 r1_p.fq -2 r2_p.fq -o assembly -meta 
    

## Tools Available

 - Trimmomatic
 - Spades
 - FastANI
 - Quast