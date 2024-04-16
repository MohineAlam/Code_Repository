# Machine learning - Supervised and unsupervised learning - whether you put in parameters or not 
    # supervised: e.g. filling out bank transactions to see if it was fraud or not is supervised
    # unsupervised e.g. programme learns inherent structure of data based off unlabeled examples

# Supervised
    # regression: trying to predict continuous valued output e.g. housing prices, value of crypto currency etc
    # Classification: trying to predict a discrete number of values e.g. is this email spam or is this picture AI or human

# Unsupervised
    # clustering: finds patterns in by grouping them into clusters e.g. social nextworks clustering topics in their news feeds

#### LINEAR REGRESSION - independent variable x (height) and find predictive value of independent variable y (weight)
    # y = g(x)
    # use training data set to infer what the function g should be
    # can now use learned function g to predict values y, for new values x
    # finding the right function g is called REGRESSION -  easiest way to find it is to assume g is linear therefore we call it linear regression
    # so we need to know slope of the line and the intercept of the line to make linear regression
        # we just need to make the slope (gradient) and intercept fit the data as much as possible
        # consider where the point of where the data points are and where it should be according to the line, take square of the difference and the sum of all the data points - take the gradient and y intercept that makes this quantity as small as possible and set it to zero

# Linear regression algorithm ####
import matplotlib.pyplot as plt
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

#slope:
m = 10
#intercept:
b = 50

#plt.plot(months, revenue, "o")
#plt.show()

# tutorial - linear regression
# list comprehension -  determine line of best fit = a line is determined by its y-intercept and slope
# y=mx+b  LINE: m = slope, b = y intercept, x is value on x-xis
    # where m is the slope, and b is the intercept. 
    # y is a given point on the y-axis, and it corresponds to a given x on the x-axis.
y = [month*m + b for month in months]

# plot y value against month
plt.plot(months,y)
plt.show()

# tutorial - linear regression
# loss = for each data point we calculate a loss - how bad the model prediction was
# see which model fits the data best

x = [1, 2, 3]
y = [5, 1, 3]

#y = x
m1 = 1
b1 = 0

#y = 0.5x + 1
m2 = 0.5
b2 = 1

# tutorial - predicting values
y_predicted1 = [m1*x_value + b1 for x_value in x]
y_predicted2 = [m2*x_value + b2 for x_value in x]

total_loss1 = 0
total_loss2 = 0

for i in range(len((y))):
  total_loss1 += (y[i] - y_predicted1[i])**2
  total_loss2 += (y[i] - y_predicted2[i])**2
 
print("total loss one:",total_loss1,". And total loss two:",total_loss2)

better_fit = 2
#########################################################################################
# tutorial - make a gradient to minimising loss = gradient descent - move in direction to decrease loss
    # N is the number of points you have in your dataset
    # m is the current gradient guess
    # b is the current intercept guess
# To find the m gradient:
    # we find the sum of x_value * (y_value - (m*x_value + b)) for all the y_values and x_values we have
    #and then we multiply the sum by a factor of -2/N. N is the number of points we have.
##########################################################################################
# Once we have a way to calculate both the m gradient and the b gradient, we’ll be able to follow both of those gradients downwards to the point of lowest loss for both the m value and the b value. Then, we’ll have the best m and the best b to fit our data!
 # we find the sum of x_value * (y_value - (m*x_value + b)) for all the y_values and x_values we have
  # and then we multiply the sum by a factor of -2/N. N is the number of points we have.

def get_gradient_at_b(x,y,m,b):
  diff = 0
  N = len(x)
  for i in range(0,len(x)):
    y_value = y[i]
    x_value = x[i]
    diff += (y_value-((m*x_value)+b))
    b_gradient = ((-2/N)*diff)
  return b_gradient

def get_gradient_at_m(x,y,m,b):
  diff = 0
  N = len(x)
  for i in range(0,len(x)):
    y_value = y[i]
    x_value = x[i]
    diff += (x_value*(y_value-((m*x_value)+b)))
    m_gradient = (diff*(-2/N))
  return m_gradient

# ------------------------------------------------------------------------------------------------------------------
# now we know how to calculate the gradient, we want to take a step in that direction
    # we dont want the step to be too big or too small, overshooting the error
        # scale the size of the step by multiplying the gradient by a learning rate - lr is proportional to the step we want to take

# find gradient using lemonade stand revenue
# here you created the gradient and the step gradient you will take
def get_gradient_at_b(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
    x_val = x[i]
    y_val = y[i]
    diff += (y_val - ((m * x_val) + b))
  b_gradient = -(2/N) * diff  
  return b_gradient

def get_gradient_at_m(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
      x_val = x[i]
      y_val = y[i]
      diff += x_val * (y_val - ((m * x_val) + b))
  m_gradient = -(2/N) * diff  
  return m_gradient

# Define your step_gradient function here
#
# tutorial
def step_gradient(x,y,b_current,m_current):
  b_gradient = get_gradient_at_b(x,y,b_current,m_current)
  m_gradient = get_gradient_at_m(x,y,m_current,b_current)
  b = b_current - (0.01*b_gradient)
  m = m_current - (0.01*m_gradient)
  return [b, m]
  print(b, m)
#
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

# current intercept guess:
b = 0
# current slope guess:
m = 0

# Call your function here to update b and m
b,m = step_gradient(months,revenue,b,m)
print(b,m)

#############################################################
# calculate gradient and move in that direction with step size proportional to learning rate
# make these steps until you reach the convergence
import matplotlib.pyplot as plt

def get_gradient_at_b(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
    x_val = x[i]
    y_val = y[i]
    diff += (y_val - ((m * x_val) + b))
  b_gradient = -(2/N) * diff  
  return b_gradient

def get_gradient_at_m(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
      x_val = x[i]
      y_val = y[i]
      diff += x_val * (y_val - ((m * x_val) + b))
  m_gradient = -(2/N) * diff  
  return m_gradient

#Your step_gradient function here
def step_gradient(b_current, m_current, x, y,learning_rate):
    b_gradient = get_gradient_at_b(x, y, b_current, m_current)
    m_gradient = get_gradient_at_m(x, y, b_current, m_current)
    b = b_current - (learning_rate * b_gradient)
    m = m_current - (learning_rate * m_gradient)
    return [b, m]
  
#Your gradient_descent function here:  

def gradient_descent(x,y,learning_rate,num_iterations):
  b = 0
  m = 0
  for iteration in range(num_iterations):
   b,m = step_gradient(b,m,x,y,learning_rate)
  return [b,m]

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

#Uncomment the line below to run your gradient_descent function
b, m = gradient_descent(months, revenue, 0.01, 1000)

#Uncomment the lines below to see the line you've settled upon!
y = [m*x + b for x in months]

plt.plot(months, revenue, "o")
plt.plot(months, y)

plt.show()
 