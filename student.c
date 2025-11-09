// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract student{
    //Structure 
    struct studentdata{
        string name;
        uint256 rollno;

    }
    //Array
    studentdata[] public studentarr;
    function addstudent(string memory name , uint256 rollno) public {
          for(uint i = 0 ; i < studentarr.length; i++){
            if(studentarr[i].rollno == rollno){
                revert("Student with this roll no already exists");  
            }
          }
          studentarr.push(studentdata(name,rollno));

    }
    function getstudentlength() public view returns (uint){
        return studentarr.length;
    }
    function displayallstudent() public view returns (studentdata[] memory) {
    studentdata[] memory result = new studentdata[](studentarr.length);
    for (uint i = 0; i < studentarr.length; i++) {
        result[i] = studentarr[i];
    }
    return result;
}
    function getstudentbyindex(uint idx)public view  returns (studentdata memory){
        require(idx < studentarr.length,"index out of bound");
        return studentarr[idx];
    }
 
 
    //fallback
    fallback() external payable { 
        //this fuction will external fuction calls that is not there in our contract
     
    }
    receive() external payable {
        //this fuction will handle the ether sent by external user but without data mentioned
     }

}
    

