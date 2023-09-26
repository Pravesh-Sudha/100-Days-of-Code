# Day 33 of 100DaysofCode

Feeling excited to start Day 33 of 100 DaysOfCode, today, I watched [Complete Web3 Bootcamp to get you a High Paying JOB in 2023](https://youtu.be/ERAxd8gl1Eg?si=ooQK02crdzROhEpj) Part-3 by <b>Harkirat Singh</b>. This video contains beginner guide to Web3 technologies, solidity basics, added functionality of level in zombieFactory application and many more.

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-33
```
## ZombieFactory.sol Explanation

- **Contract Name**: ZombieFactory
- **Solidity Version**: Greater than or equal to `0.5.0` and less than `0.6.0`
- **Inherits from**: `Ownable` contract

### Contract Structure

### State Variables

```solidity
uint dnaDigits = 16;
uint dnaModulus = 10 ** dnaDigits;
uint cooldownTime = 1 days;
```

- `dnaDigits`: An unsigned integer (uint) variable set to `16`, defining the number of digits in a zombie's DNA.
- `dnaModulus`: An unsigned integer (uint) variable calculated as `10` raised to the power of `dnaDigits`, used for DNA randomness calculations.
- `cooldownTime`: An unsigned integer (uint) variable set to `1 days`, representing the cooldown time for zombie creation.

### Struct

```solidity
struct Zombie {
    string name;
    uint dna;
    uint32 level;
    uint32 readyTime;
}
```

- `Zombie`: A custom-defined struct representing a zombie. It has four fields:
  - `name`: A string representing the name of the zombie.
  - `dna`: An unsigned integer (uint) representing the DNA of the zombie.
  - `level`: An unsigned 32-bit integer (uint32) representing the level of the zombie.
  - `readyTime`: An unsigned 32-bit integer (uint32) representing the time when the zombie is ready for action.

### Events

```solidity
event NewZombie(uint zombieId, string name, uint dna);
```

- `NewZombie`: An event triggered whenever a new zombie is created. It includes three parameters:
  - `zombieId`: An unsigned integer (uint) representing the unique ID of the newly created zombie.
  - `name`: A string representing the name of the zombie.
  - `dna`: An unsigned integer (uint) representing the DNA of the zombie.

### Functions

```solidity
function _createZombie(string memory _name, uint _dna) internal {
    uint id = zombies.push(Zombie(_name, _dna, 1, uint32(now + cooldownTime))) - 1;
    zombieToOwner[id] = msg.sender;
    ownerZombieCount[msg.sender]++;
    emit NewZombie(id, _name, _dna);
}

function createRandomZombie(string memory _name) public {
    require(ownerZombieCount[msg.sender] == 0);
    uint randDna = _generateRandomDna(_name);
    randDna = randDna - randDna % 100;
    _createZombie(_name, randDna);
}
```

- `_createZombie(string memory _name, uint _dna) internal`: An internal function used to create a new zombie. It takes two parameters: `_name` (a string) and `_dna` (an unsigned integer). It pushes a new `Zombie` struct with the given name, DNA, level, and ready time into the `zombies` array, assigns ownership to the sender, and updates the owner's zombie count. It also emits a `NewZombie` event.

- `createRandomZombie(string memory _name) public`: A public function that allows users to create a new zombie with certain conditions. It checks if the caller has no existing zombies (cooldown) and generates a random DNA with some modifications before creating the zombie using `_createZombie`.

## New Features and Changes

- **Zombie Level**: The `Zombie` struct now includes a `level` field to represent the level of the zombie.

- **Cooldown Mechanism**: Users are required to have no existing zombies (cooldown) before creating a new one, preventing rapid creation of zombies.

- **Ready Time**: The `Zombie` struct includes a `readyTime` field to track when a zombie is ready for action, incorporating a cooldown mechanism.

## ZombieFeeding.sol Explanation

## Contract Overview

- **Contract Name**: ZombieFeeding
- **Solidity Version**: Greater than or equal to `0.5.0` and less than `0.6.0`
- **Imports**: `zombiefactory.sol`
- **Interface**: `KittyInterface` for interfacing with another contract (presumably a CryptoKitties contract)

## Contract Improvements

### 1. KittyInterface Integration

```solidity
contract KittyInterface {
  // ...
}
```

- The `KittyInterface` contract is introduced, allowing interaction with external CryptoKitties contracts. This contract defines the required functions and data structures to interact with CryptoKitties, enabling the feeding of zombies with CryptoKitties' genetic data.

### 2. `setKittyContractAddress` Function

```solidity
function setKittyContractAddress(address _address) external onlyOwner {
  // ...
}
```

- A new function `setKittyContractAddress` is added, which allows the owner of the contract to set the address of the CryptoKitties contract. This address is used to interface with CryptoKitties and retrieve genetic data.

### 3. `_triggerCooldown` Function

```solidity
function _triggerCooldown(Zombie storage _zombie) internal {
  // ...
}
```

- The `_triggerCooldown` function is introduced as an internal function. It updates the `readyTime` of a zombie, implementing a cooldown mechanism for zombies after actions are performed on them.

### 4. `feedAndMultiply` Function

```solidity
function feedAndMultiply(uint _zombieId, uint _targetDna, string memory _species) public {
  // ...
}
```

- The `feedAndMultiply` function is enhanced to accept additional parameters. It checks if the sender of the transaction owns the zombie (`msg.sender == zombieToOwner[_zombieId]`) before proceeding.

- It calculates a new DNA for the zombie by combining the zombie's DNA and the target DNA. The `_species` parameter is introduced, allowing for different behaviors depending on the species being fed (e.g., "kitty").

- If the species is "kitty," the new DNA is adjusted to create a hybrid zombie with traits from both zombies.

### 5. `feedOnKitty` Function

```solidity
function feedOnKitty(uint _zombieId, uint _kittyId) public {
  // ...
}
```

- The `feedOnKitty` function is added, which interfaces with the CryptoKitties contract to retrieve the genetic data of a specified CryptoKitty (`kittyContract.getKitty(_kittyId)`) and feeds it to the `feedAndMultiply` function. This allows zombies to feed on CryptoKitties and potentially inherit some of their traits.

## ZombieHelper.sol Explanation

## Contract Overview

- **Contract Name**: ZombieHelper
- **Solidity Version**: Greater than or equal to `0.5.0` and less than `0.6.0`
- **Imports**: `zombiefeeding.sol`

## Contract Purpose

The `ZombieHelper` contract extends the functionality of the previous contracts (e.g., `ZombieFeeding`) by introducing additional features that allow users to manage and customize their zombies.

## Contract Features

### Modifier: `aboveLevel`

```solidity
modifier aboveLevel(uint _level, uint _zombieId) {
    require(zombies[_zombieId].level >= _level);
    _;
}
```

- The `aboveLevel` modifier is defined, which checks if a zombie's level is equal to or higher than a specified level before allowing a function to execute. This modifier is used to restrict certain operations to higher-level zombies.

### Function: `changeName`

```solidity
function changeName(uint _zombieId, string calldata _newName) external aboveLevel(2, _zombieId) {
    require(msg.sender == zombieToOwner[_zombieId]);
    zombies[_zombieId].name = _newName;
}
```

- The `changeName` function allows the owner of a zombie to change its name. However, this operation is restricted to zombies with a level of 2 or higher, as specified by the `aboveLevel` modifier. The function checks if the sender of the transaction owns the zombie before updating its name.

### Function: `changeDna`

```solidity
function changeDna(uint _zombieId, uint _newDna) external aboveLevel(20, _zombieId) {
    require(msg.sender == zombieToOwner[_zombieId]);
    zombies[_zombieId].dna = _newDna;
}
```

- The `changeDna` function allows the owner of a zombie to change its DNA. Similar to `changeName`, this operation is restricted to zombies with a higher level (level 20 or higher). The function checks ownership before updating the zombie's DNA.

### Function: `getZombiesByOwner`

```solidity
function getZombiesByOwner(address _owner) external view returns(uint[] memory) {
    uint[] memory result = new uint[](ownerZombieCount[_owner]);
    uint counter = 0;
    for (uint i = 0; i < zombies.length; i++) {
        if (zombieToOwner[i] == _owner) {
            result[counter] = i;
            counter++;
        }
    }
    return result;
}
```

- The `getZombiesByOwner` function allows users to retrieve an array of zombie IDs owned by a specific address. It iterates through the `zombies` array and populates the `result` array with zombie IDs owned by the specified address.

### Ownable.sol Explanation

## Contract Overview

- **Contract Name**: Ownable
- **Solidity Version**: Greater than or equal to `0.5.0` and less than `0.6.0`

## Contract Purpose

The `Ownable` contract is designed to provide basic authorization control functions, making it easier to implement user permissions in smart contracts. It defines an owner address and includes functions to check ownership, transfer ownership, and renounce ownership of a contract.

## Contract Features

### State Variable: `_owner`

```solidity
address private _owner;
```

- The `_owner` state variable is a private address that represents the owner of the contract. It is only accessible within the contract.

### Event: `OwnershipTransferred`

```solidity
event OwnershipTransferred(
    address indexed previousOwner,
    address indexed newOwner
);
```

- The `OwnershipTransferred` event is emitted whenever ownership of the contract is transferred from one address to another. It includes parameters for the previous owner and the new owner, allowing external parties to track ownership changes.

### Constructor: `constructor()`

```solidity
constructor() internal {
    _owner = msg.sender;
    emit OwnershipTransferred(address(0), _owner);
}
```

- The constructor initializes the contract by setting the original owner to the sender of the contract deployment transaction. It emits an `OwnershipTransferred` event to indicate the ownership transfer.

### Function: `owner()`

```solidity
function owner() public view returns(address) {
    return _owner;
}
```

- The `owner` function is a public view function that allows external parties to query the current owner's address.

### Modifier: `onlyOwner`

```solidity
modifier onlyOwner() {
    require(isOwner());
    _;
}
```

- The `onlyOwner` modifier is used to restrict certain functions to be callable only by the owner of the contract. It checks if the sender of the transaction is the current owner before allowing the function to execute.

### Function: `isOwner()`

```solidity
function isOwner() public view returns(bool) {
    return msg.sender == _owner;
}
```

- The `isOwner` function is a public view function that checks if the sender of the transaction is the current owner. It returns `true` if the sender is the owner and `false` otherwise.

### Function: `renounceOwnership()`

```solidity
function renounceOwnership() public onlyOwner {
    emit OwnershipTransferred(_owner, address(0));
    _owner = address(0);
}
```

- The `renounceOwnership` function allows the current owner to relinquish control of the contract. It emits an `OwnershipTransferred` event to indicate the ownership transfer to address `0x0`, effectively leaving the contract without an owner. After renouncing ownership, functions with the `onlyOwner` modifier cannot be called.

### Function: `transferOwnership(address newOwner)`

```solidity
function transferOwnership(address newOwner) public onlyOwner {
    _transferOwnership(newOwner);
}
```

- The `transferOwnership` function allows the current owner to transfer control of the contract to a new owner. It calls the internal `_transferOwnership` function to perform the ownership transfer.

### Function: `_transferOwnership(address newOwner)`

```solidity
function _transferOwnership(address newOwner) internal {
    require(newOwner != address(0));
    emit OwnershipTransferred(_owner, newOwner);
    _owner = newOwner;
}
```

- The `_transferOwnership` function is an internal function that handles the actual transfer of ownership. It requires that the new owner's address is not `0x0`, emits an `OwnershipTransferred` event to record the ownership change, and updates the `_owner` state variable.
