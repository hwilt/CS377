import os

class FileWriter:
  """
  Construct a FileWriter

  :param _filename: The filename to open
  :param _append: Whether to append to the file or overwrite
  """
  def __init__(self, _filename, _append=True):
    self.filename = _filename

    if _append:
      mode = 'a+'
    else:
      mode = 'w'

    self.f = open(self.filename, mode)

  """ 
  Destructor: flush and close the file 
  """
  def __del__(self):
    self.f.flush()
    self.f.close()    

  """
  Write a dictionary row, writing the keys as the header line if the file is empty.

  :param data: The dictionary to write - must be a dict
  :raises TypeError: if the data parameter is a type other than dict
  """
  def write_record(self, data):
    if isinstance(data, dict): # ensure data is a dict
      # write header if the file is empty
      if os.stat(self.filename).st_size == 0:
        self.f.write(','.join(data.keys()))
        # write a newline
        self.f.write("\n")

      # write each element of the row separated by commas,
      # converting all values to strings
      self.f.write(','.join(str(x) for x in data.values()))

      # write a newline
      self.f.write("\n")

      # flush the file contents so that the size is correct next time we check 
      # ... when writing the header
      # TODO a better idea would be to store a boolean that represents whether the
      # ... file is empty, so that we can gain some I/O efficiency by not flushing
      # ... on every write, using memory instead to buffer
      self.f.flush()
    else:
      return TypeError("Data must be a dict")