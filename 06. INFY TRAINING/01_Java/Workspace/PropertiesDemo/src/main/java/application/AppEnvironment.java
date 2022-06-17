package application;

import java.util.Iterator;

import org.apache.commons.configuration2.PropertiesConfiguration;
import org.apache.commons.configuration2.builder.fluent.Configurations;

public class AppEnvironment {
	public static void main(String[] args) throws Exception {

		PropertiesConfiguration config = null;
		Configurations configurations = new Configurations();
		config = configurations.properties("configuration.properties");
		// Fetching all the key-value pairs from the properties file
		System.out.println("---- Fetching all the key value pairs ----");
		Iterator<String> keysInPropsFile = config.getKeys();
		System.out.println(keysInPropsFile);
		while (keysInPropsFile.hasNext()) {
			String key = keysInPropsFile.next();
			System.out.println(key + " = " + config.getProperty(key));
		}
		
		
		System.out.println("---- Fetching a single value by passing the key ----");
		System.out.println("Value for server.port=" + config.getProperty("server.port"));
		// Calculating sum from two number values stored in .properties file
		// Since the return type of getProperty() is an object, you have to type-cast it
		// accordingly
		Integer value1 = Integer.parseInt((String) config.getProperty("value1"));
		Integer value2 = Integer.parseInt((String) config.getProperty("value2"));
		Integer sum = value1 + value2;
		System.out.println("Sum=" + sum);

	}

}
