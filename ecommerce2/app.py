
### To import the shipping module
#import ecommerce2.shipping

### Use function from shipping module
#ecommerce2.shipping.calc_shipping()

# ---------------------------------
### More efficient than above
#from ecommerce2.shipping import calc_shipping
#calc_shipping()
# ---------------------------------
### Even more and more efficient
from ecommerce2 import shipping     #import all from shipping
shipping.calc_shipping()