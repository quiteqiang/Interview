# Careeir interview

### This is a repo where I practice Interciew questions

#### Object-oriented programming
1. OOP is faster and easier to execute
2. OPP provides a clear structure for the programs
3. OPP helps to keep the Java code "DRY" (Don;t repeat yourself), makes the code easier to maintain, modify, and debug
4. Create reusable applications with less code and shorter development time 


#### Static VS Non-static
1. static method, means that it can be accessed without creating an object of 
the class
2. public method, which can only be accessed by objects

#### Constructor
1. Used to initizlize objects 
2. The constructor is called when an object of a class is created.

#### Modifier
1. Access Modifiers
2. Non-Access Modifuers

##### Access Modifier
1. public: class is accessible by any other class
2. default: don't specify "public", class only accessible by classes in the same package
3. private: code is only accessible within the declared class
4. protected: The code is accessible in the same package and subclasses(inherent).

##### Non-Access Modifiers
1. Class: final, abstract; attributes,methods: final, static, abstract, transient
synchronized, volatile
2. final: attributes and methods cannot be overidden/modified
3. static:Attributes and methods belongs to the class, rather than object
4. abstract: only in abstract class, only in methods
5. transient: Attributes and methods are skipped when serializing the object containing them
6. synchronized: 	Methods can only be accessed by one thread at a time
7. The value of an attribute is not cached thread-locally, and is always read from the "main memory" 



##### Java Packages
1. Built-in packages (packages from java API, inclding Java Development Ecnironment)
2. User0defined packages 
	1. Use package package-name in the begining of the file
	2. save as java file
	3. compile the package: javac -d . mypackage.java

##### Java Inheritance
1. subclass(child) the class that inherits from another class
2. superclass(parent) the class being inherited from
3. 'final' can be used to prevent from the class being inherienteed

##### Java Polymorphism (many forms )
 Seperate methoeds in multiple classes

##### Java inner class
1. Nest classes(a class within another class)
2. Group classes that blong together, code more readble and maintainable
3. The inner class can be private or protected, 'private' can prevent from accessing from outer-class
4. 'static' can be used for the inner class, it can be accessed without creating an objet of the outer class
5. Access outer class from the inner class:  

##### Java Abstraction
1. Hiding certain details and show essential information to the user
2. Abstract class: cannot be used to create objects, can accessed by inheriting
3. Abstract method: only used in abstract class, has no body, body is provided by subclass

##### Java Interface
1. An 'interface' is completely "abstract class" that is used to group related methoed with empty bodies. 
2.'Why use Interface', achieve security, hide details and show necessary details of an object; support 'multiple inheritance'.























