## Circular Dependency Article Examples

The article these examples pertain to can be found here.

## How to Run Examples 

There are two ways to run the examples, depending on if you have direct shell access or not on the platform you're using to access Replit. In any case, if the point of the example you are running is to throw an error... Then it's going to throw an error. 

### I have direct shell access

Make sure your current working directory is the project root (i.e. the same one this `README.md` file is in) and then type `python -m <example-directory-name>`. Obviously replace the last part with the name of the example directory you want to run. 

Example: `python -m chicken-egg-example`

### I don't have direct shell access 

You'll need to edit the run script to reflect the example you want to run. 

The run script is located in the `.replit` file in the root directory. Edit it to reflect the example that you want to run. For example: 

``` 
run = "python -m chicken-egg-example"
```

Then hit the run button.