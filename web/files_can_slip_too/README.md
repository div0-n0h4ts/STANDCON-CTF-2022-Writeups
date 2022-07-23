# Files can Slip too

**Author:** SecurityGOAT

## Category

Web

## Question

> Files say a lot and can do a lot, but did you knew that files can slip too? Provided the surface is slippery enough.  

## Hints

1. Can a make a Zip archive with relative file paths?
2. What happens if the server extracts files with relative paths? Can the extracted files somehow *slip* the file upload directory?



## Solution

Upload a zip archive with relative path to add the **evil.php** file in the webroot directory.  

**Note:** Challenge has been updated and the flag file is now located at: **flag_022dc5a58d33**.  

### Detailed Solution

![1](solution/1.png)

Uploading a zip file containing one file:  

![2](solution/2.png)

The file is extracted:  

![3](solution/3.png)

Open the extracted file:  

![4](solution/4.png)

It is extracted in the following path: **uploads/extracted/<zip_file_name>/<file_name>**.  

Create a malicious zip archive with a PHP webshell that has a relative path containing 3 **../** sequences to jump out of the created directory structure:  

![5](solution/5.png)

Upload this malicious zip archive:  

![6](solution/6.png)

Zip file is uploaded and extracted:  

![7](solution/7.png)

Open link to the extracted **evil.php** file:  

![8](solution/8.png)

The page works. Send a shell command:  

![9](solution/9.png)

Webshell is successfully uploaded!  

Get the flag:  

![10](solution/10.png)

![11](solution/11.png)


## Flag
STANDCON22{uns4f3_z!p_3xtr4c7!0n_!5_4_r34l_d4ng3r}