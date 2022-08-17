# Contributing

## Style & Formatting
This project will mainly adhere to the style guide referenced in [PEP 8](https://peps.python.org/pep-0008/#naming-conventions)

### General Conventions
* Max line length will be 99 characters
* Max docstring length will be 72 characters
* Always use UTF-8 encoding

<details>
  <summary>Indentation</summary>
  
  ### Indentation
  This project will use 4 **spaces** (not tabs) for indentation level
  ```python
  def some_function():
      some_value_one = 1
      some_value_two = 2
      return some_value_one + some_value_two
  ```
  Method parameters and function arguments will align with the opening delimiter when the line would otherwise be too long
  ```python
  # method signature fits on one line
  def short_method(some_param):
      # ...do something in method
  
  # method signature too long to fit on one line
  # align parameters with opening parenthesis
  def long_method(param_one, param_two, param_three
                  param_four, param_five, param_six):
      # ...do something in method
  
  # method call too long to fit on one line
  # align arguments with opening parenthesis
  long_method(arg_one, arg_two, arg_three, arg_four
              arg_five, arg_six)
  
  ```
  Long conditional statements will follow similar conventions to method signatures where continuations are aligned with the opening delimiter. Any operators will remain at the end of the previous line.
  ```python
  # 'and' operator remains on the previous line
  if (some_boolean_value and
      some_other_boolean_value):
  ```
  Objects that are multiline will have the closing delimiter align with the beginning line of the construct
  ```python
  # closing square bracket lines up with array declaration
  my_arr = [
      1, 2, 3,
      4, 5, 6,
  ]
  
  # closing curly bracket lines up with dictionary declaration
  my_dict = {
      "key1": "value1",
      "key2": "value2",
  }
  ```
</details>

<details>
  <summary>Naming</summary>
  
  ## Naming
  Abbreviations **should be avoided** wherever possible. Being explicit will improve readability for onboarding contributors 
  ```python
  # avoid
  def test_throws_val_err_on_bad_input():
  
  # non-abbreviated
  def test_throws_value_error_when_given_wrong_input_type():
  ```
  When naming modules, use all lowercase characters and underscores if necessary
  ```
  my_module.py
  ```
  When naming packages, use all lowercase characters and *avoid* underscores if possible
  ```
  mypackage
  ```
  
</details>
