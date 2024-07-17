
# import modules 
from matplotlib_venn import venn2  
from matplotlib import pyplot as plt 
  
# depict venn diagram 
venn2(subsets = (50, 10, 7), set_labels = ('Group A', 'Group B')) 
plt.show()