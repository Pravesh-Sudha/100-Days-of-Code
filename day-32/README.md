# Day 32 of 100DaysofCode

Feeling excited to start Day 32 of 100 DaysOfCode, today, I watched [Complete Web3 Bootcamp to get you a High Paying JOB in 2023](https://youtu.be/ERAxd8gl1Eg?si=ooQK02crdzROhEpj) Part-2 by <b>Harkirat Singh</b>. This video contains beginner guide to Web3 technologies, solidity basics, What is Ethereum, how web3 works, smart contracts and many more.

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-32
```

## Zombie Factory Smart Contract (zombiefactory.sol)

This README file provides an explanation of the `ZombieFactory.sol` smart contract. The contract is written in Solidity, a programming language used for developing smart contracts on the Ethereum blockchain.

### Prerequisites

Before diving into the contract explanation, please ensure that you have a basic understanding of Solidity, Ethereum, and smart contracts.

### Overview

The `ZombieFactory` contract is a simple example of a blockchain-based application that allows users to create and own unique virtual zombies. Each zombie has a name and DNA represented as a 16-digit number. Users can create a random zombie with a unique combination of name and DNA. 

### Contract Structure

#### Version Declaration

```solidity
pragma solidity >=0.5.0 <0.6.0;
```

This line specifies the version of Solidity the contract is compatible with.

#### Contract Definition

```solidity
contract ZombieFactory {
    // ...
}
```

The `ZombieFactory` contract is defined here.

#### State Variables

```solidity
    uint dnaDigits = 16;
    uint dnaModulus = 10 ** dnaDigits;
```

- `dnaDigits` specifies the number of digits in a zombie's DNA.
- `dnaModulus` is a constant used to calculate the DNA, as it determines the maximum possible DNA value.

#### Struct Definition

```solidity
    struct Zombie {
        string name;
        uint dna;
    }
```

This `Zombie` struct defines the structure of a zombie. It consists of two fields: `name` (a string) and `dna` (an unsigned integer).

#### Public Arrays

```solidity
    Zombie[] public zombies;
```

- `zombies` is an array of `Zombie` structs, and it is publicly accessible.

#### Mappings

```solidity
    mapping (uint => address) public zombieToOwner;
    mapping (address => uint) ownerZombieCount;
```

- `zombieToOwner` maps zombie IDs to the addresses of their owners.
- `ownerZombieCount` maps addresses to the number of zombies owned by each address.

#### Internal Function

```solidity
    function _createZombie(string memory _name, uint _dna) internal {
        // ...
    }
```

- `_createZombie` is an internal function used to create a new zombie. It takes a name and DNA as arguments, adds the new zombie to the `zombies` array, updates the owner and count mappings, and emits a `NewZombie` event.

#### Private Function

```solidity
    function _generateRandomDna(string memory _str) private view returns (uint) {
        // ...
    }
```

- `_generateRandomDna` is a private view function used to generate random DNA based on a provided string `_str`. It uses a hashing function to create pseudo-randomness.

#### Public Function

```solidity
    function createRandomZombie(string memory _name) public {
        // ...
    }
```

- `createRandomZombie` is a public function that allows users to create a random zombie with the given `_name`. It checks if the caller owns any zombies and then generates a random DNA for the new zombie using `_generateRandomDna`. Finally, it calls `_createZombie` to create the new zombie.

### Events

```solidity
    event NewZombie(uint zombieId, string name, uint dna);
```

- `NewZombie` is an event that is emitted whenever a new zombie is created. It logs the zombie's ID, name, and DNA for external monitoring.

## Zombie Feeding Smart Contract (zombiefeeding.sol)

This README file provides an explanation of the `ZombieFeeding.sol` smart contract. This contract extends the functionality of the `ZombieFactory` contract by allowing zombies to feed on external entities, particularly kitties. The contract is written in Solidity, a programming language used for developing smart contracts on the Ethereum blockchain.

### Prerequisites

Before diving into the contract explanation, please ensure that you have a basic understanding of Solidity, Ethereum, and smart contracts. Additionally, this contract relies on the `KittyInterface` contract and the `ZombieFactory` contract, which should be deployed and accessible.

### Overview

The `ZombieFeeding` contract is designed to allow zombies to feed on external entities, specifically kitties. When a zombie feeds on a kitty, its DNA is modified based on the kitty's genetic information. The contract uses the `KittyInterface` to interact with an external contract that provides information about kitties.

### Contract Structure

#### Version Declaration

```solidity
pragma solidity >=0.5.0 <0.6.0;
```

This line specifies the version of Solidity the contract is compatible with.

#### Import Statements

```solidity
import "./zombiefactory.sol";
```

This line imports the `ZombieFactory` contract, indicating that `ZombieFeeding` extends its functionality.

#### External Contract Interface

```solidity
contract KittyInterface {
  // ...
}
```

This contract interface defines the required functions for interacting with the external contract that handles kitties. It specifies the expected data structure for a kitty's information.

#### Contract Definition

```solidity
contract ZombieFeeding is ZombieFactory {
    // ...
}
```

The `ZombieFeeding` contract is defined here, inheriting from `ZombieFactory` to reuse its functionality.

#### State Variables

```solidity
  address ckAddress = 0x06012c8cf97BEaD5deAe237070F9587f8E7A266d;
  KittyInterface kittyContract = KittyInterface(ckAddress);
```

- `ckAddress` is the address of the external kitty contract.
- `kittyContract` is an instance of the `KittyInterface` contract that allows interactions with the kitty contract at `ckAddress`.

#### Public Functions

#### `feedAndMultiply`

```solidity
function feedAndMultiply(uint _zombieId, uint _targetDna, string memory _species) public {
    // ...
}
```

- This function takes three parameters: `_zombieId`, `_targetDna`, and `_species`.
- It checks if the caller is the owner of the zombie specified by `_zombieId`.
- It retrieves the zombie's data, modifies the DNA based on the provided `_targetDna`, and creates a new zombie with the modified DNA.
- If `_species` is "kitty," it ensures that the new DNA is a multiple of 100 to represent a kitty influence.

#### `feedOnKitty`

```solidity
function feedOnKitty(uint _zombieId, uint _kittyId) public {
    // ...
}
```

- This function takes two parameters: `_zombieId` and `_kittyId`.
- It calls the external `kittyContract` to retrieve the genetic information of the kitty specified by `_kittyId`.
- Then, it calls `feedAndMultiply` with the zombie's ID and the kitty's DNA, specifying the `_species` as "kitty."
