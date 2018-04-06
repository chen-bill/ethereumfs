pragma solidity ^0.4.13;

contract EthereumFS {
  mapping(address => mapping(uint => file)) fs;
  struct file {
    uint start;
    uint len;
  }
  
  function getFile(uint fileIndex) constant returns (uint start, uint length){
      return (fs[msg.sender][fileIndex].start, fs[msg.sender][fileIndex].len);
  }
  
  function updateFile(uint fileIndex, uint start, uint length) returns (bool) {
      fs[msg.sender][fileIndex].start = start;
      fs[msg.sender][fileIndex].len = length;
      return true;
  }
}
