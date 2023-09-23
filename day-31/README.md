# Day 31 of 100DaysofCode

Feeling excited to start Day 31 of 100 DaysOfCode, today, I watched [Complete Web3 Bootcamp to get you a High Paying JOB in 2023](https://youtu.be/ERAxd8gl1Eg?si=ooQK02crdzROhEpj) Part-1 by <b>Harkirat Singh</b>. This video contains beginner guide to Web3 technologies, solidity basics, What is Ethereum, how web3 works, smart contracts and many more.

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-31
```

# Understanding Web3, Ethereum, and Smart Contracts

## Table of Contents
- [Introduction](#introduction)
- [Web3](#web3)
- [Ethereum](#ethereum)
- [Smart Contracts](#smart-contracts)
- [How They Work Together](#how-they-work-together)
- [Getting Started](#getting-started)
- [Resources](#resources)

## Introduction

In the world of blockchain technology and decentralized applications (dApps), understanding the concepts of Web3, Ethereum, and smart contracts is essential.

## Web3

**Web3** refers to a set of protocols and libraries that enable interactions with the Ethereum blockchain and other blockchain networks. It allows developers to build decentralized applications (dApps) that can interact with smart contracts and the Ethereum network without relying on centralized servers.

Web3.js is a popular JavaScript library used for Web3 development. It provides APIs for connecting to Ethereum nodes, sending transactions, and interacting with smart contracts.

## Ethereum

**Ethereum** is a decentralized blockchain platform created by Vitalik Buterin in 2015. Unlike Bitcoin, which primarily serves as a digital currency, Ethereum is designed to support smart contracts and dApps. 

Ethereum uses a cryptocurrency called Ether (ETH) to power its network. It is a public blockchain, meaning anyone can participate by running an Ethereum node, mining, or interacting with smart contracts.

## Smart Contracts

**Smart contracts** are self-executing contracts with the terms of the agreement directly written into code. They run on blockchain platforms like Ethereum and automatically execute when predefined conditions are met. Smart contracts enable trustless and transparent transactions without the need for intermediaries.

Smart contracts are typically written in programming languages like Solidity and deployed on the Ethereum blockchain. They can be used for a wide range of applications, from simple token transfers to complex decentralized applications.

## How They Work Together

1. **Web3 and Ethereum Connection**: Web3.js (or similar libraries) is used to connect your dApp to the Ethereum blockchain. This connection allows your application to interact with the Ethereum network, read data, and send transactions.

2. **Deploying Smart Contracts**: Smart contracts are written using languages like Solidity. Once written, they are compiled into bytecode and deployed to the Ethereum network. This deployment is done via a transaction on the Ethereum blockchain.

3. **Interacting with Smart Contracts**: Once deployed, smart contracts have a unique address on the Ethereum network. Your dApp can interact with these contracts by sending transactions to their address using Web3.js. These transactions can trigger functions defined within the smart contract code.

4. **Transaction Validation**: Transactions sent to smart contracts are validated by the Ethereum network's miners. If the transaction is valid and meets the predefined conditions in the smart contract, it is executed.

5. **Results and State Changes**: The execution of a smart contract can result in state changes on the Ethereum blockchain. For example, transferring tokens, updating data, or creating new records. These changes are recorded on the blockchain for transparency and immutability.

## Getting Started

To start working with Web3, Ethereum, and smart contracts, you'll need to:

1. **Set Up a Development Environment**: Install the necessary tools like Node.js, Ethereum client (such as Ganache), and a code editor.

2. **Learn Web3**: Study Web3.js or other Web3 libraries to understand how to connect to the Ethereum network in your chosen programming language.

3. **Learn Solidity**: If you plan to develop smart contracts, learn Solidity, the primary programming language for Ethereum smart contracts.

4. **Experiment**: Start by creating simple smart contracts and dApps to gain hands-on experience.

## Zombiefactory.sol Explanation

- **Contract Name**: ZombieFactory
- **Solidity Version**: Greater than or equal to `0.5.0` and less than `0.6.0`

### Contract Structure

#### State Variables

```solidity
uint dnaDigits = 16;
uint dnaModulus = 10 ** dnaDigits;
Zombie[] public zombies;
```

- `dnaDigits`: An unsigned integer (uint) variable set to `16`, which defines the number of digits in a zombie's DNA.
- `dnaModulus`: An unsigned integer (uint) variable calculated as `10` raised to the power of `dnaDigits`. This is used for DNA randomness calculations.
- `zombies`: An array of custom-defined `Zombie` structs. This array holds the zombie data for all zombies created using this contract.

#### Struct

```solidity
struct Zombie {
    string name;
    uint dna;
}
```

- `Zombie`: A custom-defined struct representing a zombie. It has two fields:
  - `name`: A string representing the name of the zombie.
  - `dna`: An unsigned integer (uint) representing the DNA of the zombie.

#### Events

```solidity
event NewZombie(uint zombieId, string name, uint dna);
```

- `NewZombie`: An event triggered whenever a new zombie is created. It includes three parameters:
  - `zombieId`: An unsigned integer (uint) representing the unique ID of the newly created zombie.
  - `name`: A string representing the name of the zombie.
  - `dna`: An unsigned integer (uint) representing the DNA of the zombie.

#### Functions

```solidity
function _createZombie(string memory _name, uint _dna) private {
    uint id = zombies.push(Zombie(_name, _dna)) - 1;
    emit NewZombie(id, _name, _dna);
}

function _generateRandomDna(string memory _str) private view returns (uint) {
    uint rand = uint(keccak256(abi.encodePacked(_str)));
    return rand % dnaModulus;
}

function createRandomZombie(string memory _name) public {
    uint randDna = _generateRandomDna(_name);
    _createZombie(_name, randDna);
}
```

- `_createZombie(string memory _name, uint _dna) private`: A private function used to create a new zombie. It takes two parameters: `_name` (a string) and `_dna` (an unsigned integer). It pushes a new `Zombie` struct with the given name and DNA into the `zombies` array and emits a `NewZombie` event.

- `_generateRandomDna(string memory _str) private view returns (uint)`: A private view function that generates a random DNA value based on the input `_str`. It uses the `keccak256` hash function to derive randomness from `_str` and then calculates the remainder when dividing by `dnaModulus`. This ensures that the resulting DNA is within the defined `dnaModulus` range.

- `createRandomZombie(string memory _name) public`: A public function that allows users to create a new zombie with a random DNA. It takes the `_name` of the zombie as input and generates a random DNA using `_generateRandomDna`. Then, it calls `_createZombie` to create a new zombie with the provided name and random DNA.


## Resources

Here are some resources to help you dive deeper into these topics:

- [Web3.js Documentation](https://web3js.readthedocs.io/en/v1.10.0/): Official documentation for Web3.js.
- [Ethereum Official Website](https://ethereum.org/): The official Ethereum website with extensive resources.
- [Solidity Documentation](https://docs.soliditylang.org/en/v0.8.6/): Official documentation for Solidity.
- [Ethereum Developer Documentation](https://ethereum.org/developers/): Comprehensive resources for Ethereum developers.
