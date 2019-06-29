{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "s='Python is easy programming to learn and intersting'\n",
    "s1=\"python\"\n",
    "print(s.islower())\n",
    "print(s1.islower())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "s=\"Application\"\n",
    "s1=\"ARJUN\"\n",
    "print(s.isupper())\n",
    "print(s1.isupper())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "s=\"5678\"\n",
    "s1=\"Application\"\n",
    "print(s.isnumeric())\n",
    "print(s1.isnumeric())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "s=\"Application\"\n",
    "s1=\"App1889\"\n",
    "print(s.isalpha())\n",
    "print(s1.isalpha())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "s=\"python programming\"\n",
    "s1=\"Python Programming\"\n",
    "print(s.istitle())\n",
    "print(s1.istitle())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "s=\"Python\"\n",
    "s1=\" \"\n",
    "print(s.isspace())\n",
    "print(s1.isspace())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "P y t h o n\n"
     ]
    }
   ],
   "source": [
    "str=\"Python\"\n",
    "print(\" \".join(str))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['python', 'programming', 'is', 'easy', 'to', 'learn']\n",
      "['python progr', 'mming is e', 'sy to le', 'rn']\n",
      "['python programming is easy to learn']\n"
     ]
    }
   ],
   "source": [
    "s=\"python programming is easy to learn\"\n",
    "print(s.split())\n",
    "print(s.split(\"a\"))\n",
    "print(s.split(\" ,\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "python,programming,easy\n"
     ]
    }
   ],
   "source": [
    "print(\",\".join([\"python\",\"programming\",\"easy\"]))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['python', 'is', 'easy', 'to', 'learn']\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "s=\"python is easy to learn\"\n",
    "lst=s.split()\n",
    "print(lst)\n",
    "print(lst.index(\"is\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['p', 'y', 't', 'h', 'o', 'n', ' ', 'i', 's', ' ', 'e', 'a', 's', 'y', ' ', 't', 'o', ' ', 'l', 'e', 'a', 'r', 'n']\n"
     ]
    }
   ],
   "source": [
    "s=\"python is easy to learn\"\n",
    "lst=list(s)\n",
    "print(lst)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "python proapplicationmming\n"
     ]
    }
   ],
   "source": [
    "s=\"python programming\"\n",
    "print(s.replace(\"gra\",\"application\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "t1[0]= python\n",
      "t1[2]= 1989\n",
      "t1[-1]= AI\n",
      "t1[1:4]= ('programming', 1989, 2019)\n",
      "t1[2:-2]= (1989, 2019)\n"
     ]
    }
   ],
   "source": [
    "t1 = (\"python\",\"programming\",1989,2019,\"Machine learning\",\"AI\")\n",
    "print(\"t1[0]=\",t1[0])\n",
    "print(\"t1[2]=\",t1[2])\n",
    "print(\"t1[-1]=\",t1[-1])\n",
    "print(\"t1[1:4]=\",t1[1:4])\n",
    "print(\"t1[2:-2]=\",t1[2:-2])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('python', 'programming', 1989, 2019, 'Machine learning', 'AI')\n",
      "(1, 2, 3, 4, 5)\n"
     ]
    }
   ],
   "source": [
    "t1 = (\"python\",\"programming\",1989,2019,\"Machine learning\",\"AI\")\n",
    "t2=(1,2,3,4,5)\n",
    "print(t1)\n",
    "print(t2)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('python', 'programming', 1989, 2019, 'ML', 'AI')\n"
     ]
    }
   ],
   "source": [
    "t1=(\"python\",\"programming\")\n",
    "t2=(1989,2019,\"ML\",\"AI\")\n",
    "t3=t1+t2\n",
    "print(t3)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1, 2, 3, 4, 5)\n",
      "(1, 2, 3, 4, 5)\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'cnp' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-24-c88043d10de3>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mt1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mt2\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 5\u001b[0;31m \u001b[0ma\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mcnp\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m: name 'cnp' is not defined"
     ]
    }
   ],
   "source": [
    "t1=(1,2,3,4,5)\n",
    "t2=(1,2,3,4,5)\n",
    "print(t1)\n",
    "print(t2)\n",
    "a=cnp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "77\n"
     ]
    }
   ],
   "source": [
    "t1=(14,16,20,1,77)\n",
    "print(max(t1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "t1=(14,16,20,1,77)\n",
    "print(min(t1))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "t1=(14,16,20,1,77)\n",
    "print(len(t1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n"
     ]
    }
   ],
   "source": [
    "t1=(14,16,20,1,77)\n",
    "print(len(t1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('python', 'programming', 1989, 2019, 'machine learning', 'AI')\n",
      "('python', 'programming', 1989, 2019, 'machine learning', 'AI')\n"
     ]
    }
   ],
   "source": [
    "t1=(\"python\",\"programming\",1989,2019,\"machine learning\",\"AI\")\n",
    "print(t1)\n",
    "tuple1=tuple(t1)\n",
    "print(tuple1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "user1[name]= anil\n",
      "user1[mobilenumber]= 4578905689\n",
      "user1[age]= 18\n",
      "user1[email]= sravani@gmail.com\n"
     ]
    }
   ],
   "source": [
    "user1={'name':\"anil\",'mobilenumber':'4578905689','mail':'sravani@gmail.com','age':'18'}\n",
    "print(\"user1[name]=\",user1['name'])\n",
    "print(\"user1[mobilenumber]=\",user1['mobilenumber'])\n",
    "print(\"user1[age]=\",user1['age'])\n",
    "print(\"user1[email]=\",user1['mail'])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "sravani@gmail.com\n",
      "sravani@gmail.com\n",
      "hyderbad\n"
     ]
    }
   ],
   "source": [
    "user1={'name':\"anil\",'mobilenumber':'4578905689','mail':'sravani@gmail.com','age':'18'}\n",
    "print(user1['mail'])\n",
    "user1['mail']='sravani@gmail.com'\n",
    "print(user1['mail'])\n",
    "user1['address']='hyderbad'\n",
    "print(user1['address'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n",
      "5\n"
     ]
    }
   ],
   "source": [
    " user1={'name':\"anil\",'mobilenumber':'4578905689','mail':'sravani@gmail.com','age':'18'}\n",
    "print(len(user1))\n",
    "user1['address']='hyderbad'\n",
    "print(len(user1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'name': 'anil', 'mobilenumber': '4578905689', 'mail': 'sravani@gmail.com', 'age': '18'}\n",
      "{'name': 'anil', 'mobilenumber': '4578905689', 'mail': 'sravani@gmail.com', 'age': '18'}\n",
      "{'name': 'anil', 'mobilenumber': '4578905689', 'mail': 'sravani@gmail.com', 'age': '18', 'address': 'hyderbad'}\n",
      "{'name': 'anil', 'mobilenumber': '4578905689', 'mail': 'sravani@gmail.com', 'age': '18'}\n"
     ]
    }
   ],
   "source": [
    "user1={'name':\"anil\",'mobilenumber':'4578905689','mail':'sravani@gmail.com','age':'18'}\n",
    "user2=user1.copy()\n",
    "print(user1)\n",
    "print(user2)\n",
    "user1[\"address\"]=\"hyderbad\"\n",
    "print(user1)\n",
    "print(user2)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dict_values(['anil', '4578905689', 'sravani@gmail.com', '18'])\n",
      "dict_values(['anil', '4578905689', 'sravani@gmail.com', '18'])\n"
     ]
    }
   ],
   "source": [
    "user1={'name':\"anil\",'mobilenumber':'4578905689','mail':'sravani@gmail.com','age':'18'}\n",
    "user2=user1.copy()\n",
    "print(user1.values())\n",
    "print(user1.values())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "python programming\n"
     ]
    }
   ],
   "source": [
    "lst=['python','programming']\n",
    "print(\"%s %s\"%(lst[0],lst[1]))\n",
    "       \n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "python programming\n"
     ]
    }
   ],
   "source": [
    "lst=['python','programming']\n",
    "print(\"{0} {1}\".format(lst[0],lst[1]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
