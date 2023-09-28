# Day 34 of 100DaysofCode

Feeling excited to start Day 34 of 100 DaysOfCode, today, I watched [Complete Web3 Bootcamp to get you a High Paying JOB in 2023](https://youtu.be/ERAxd8gl1Eg?si=ooQK02crdzROhEpj) Part-3 by <b>Harkirat Singh</b>. This video contains beginner guide to Web3 technologies, solidity basics, how payments are done in web3 and many more.

## How the project works?

Clone this repository or simply refer to the README for a quick reference on how my repository works. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/Pravesh-Sudha/100-Days-Of-Code.git
cd day-34
```

# ZombieAttack.sol Explanation

## Contract Overview

- **Contract Name**: ZombieAttack
- **Solidity Version**: Greater than or equal to `0.5.0` and less than `0.6.0`
- **Imports**: `zombiehelper.sol`

## Contract Purpose

The `ZombieAttack` contract is designed to introduce a battle system for zombies, allowing them to attack and potentially defeat other zombies. This contract inherits functionality from `ZombieHelper` and extends it with attack-related features.

## Contract Features

### State Variables

```solidity
uint randNonce = 0;
uint attackVictoryProbability = 70;
```

- `randNonce`: An unsigned integer (uint) variable initialized to `0`. It is used to generate random numbers for battle outcomes.
- `attackVictoryProbability`: An unsigned integer (uint) variable set to `70`, representing the probability of a zombie winning an attack.

### Function: `randMod`

```solidity
function randMod(uint _modulus) internal returns(uint) {
    randNonce++;
    return uint(keccak256(abi.encodePacked(now, msg.sender, randNonce))) % _modulus;
}
```

- The `randMod` function is an internal function that generates a pseudo-random number based on certain inputs. It increments the `randNonce` variable, combines the current timestamp, sender's address, and `randNonce` to create a random seed, and then calculates the modulo of the seed with the specified `_modulus`. This function is used to determine the outcome of battles.

### Function: `attack`

```solidity
function attack(uint _zombieId, uint _targetId) external ownerOf(_zombieId) {
    Zombie storage myZombie = zombies[_zombieId];
    Zombie storage enemyZombie = zombies[_targetId];
    uint rand = randMod(100);
    if (rand <= attackVictoryProbability) {
        myZombie.winCount++;
        myZombie.level++;
        enemyZombie.lossCount++;
        feedAndMultiply(_zombieId, enemyZombie.dna, "zombie");
    }
}
```

- The `attack` function allows the owner of a zombie (specified by `_zombieId`) to initiate an attack on another zombie (specified by `_targetId`). The attacking zombie's statistics are stored in `myZombie`, and the target zombie's statistics are stored in `enemyZombie`.

- A random number `rand` is generated using the `randMod` function to determine the outcome of the attack. If `rand` is less than or equal to the `attackVictoryProbability`, the attacking zombie wins the battle. In this case, the attacking zombie's win count and level are increased, and the target zombie's loss count is increased. Additionally, the `feedAndMultiply` function is called to potentially create a new zombie with traits from both the attacker and the target.

