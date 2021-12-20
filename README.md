<p align="center">
  <img src="icon.jpg" alt="icon" width=300 height=300/>
</p>


Python Secret Santa Manager
===================

This little and yet simple python repo serves the honorable job of the Secret Santa Manager!


Features
--------
* Take advantage of the simple Python's email manager defined [here](https://github.com/dimaba/sendmail);
* Can use gmail as sender mail if you set an [App password](https://support.google.com/accounts/answer/185833?hl=en) and use it;


Create a santa manager for a friends mailing list
----------------------------------
You have just to fill the  ```name_mail.json``` file with couples of name and a valid mail to receive the message. 
Remember that all the names has to be unique! For example, if you have two friends called as ```Aldo``` you have to distinguish them using something like ```Aldo_A``` and ```Aldo_B```. 

The message can be modified in the ```santa_manager_mail.py``` where also the main logic was defined. To send the e-mails you have to uncomment some lines, this is just to let you avoid send mails without a double-check of them.