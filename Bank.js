// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract Bank
{
    uint256 balance=0;
    address public  accowner;
    constructor()
{
    accowner=msg.sender;
}    
//Depoist
function Deposit() public payable {
    require(accowner==msg.sender,"you are not an aacount owner");
    require(msg.value > 0,"Amount should be grater than 0!");
    balance+=msg.value;
    }


//withdraw
function Withdraw()public payable {
    require(accowner==msg.sender,"You are not an account owner");
    require(msg.value > 0,"Withdrawal money should be grater than 0.");
    balance-=msg.value;
}

//Showbalance
function showbalance()public view  returns(uint256){
    require(accowner==msg.sender,"You are not an account ower");
    return balance;
}
}
