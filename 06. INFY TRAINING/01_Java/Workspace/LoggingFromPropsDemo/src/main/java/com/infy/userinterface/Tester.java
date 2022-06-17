package com.infy.userinterface;

import org.apache.commons.configuration2.PropertiesConfiguration;
import org.apache.commons.configuration2.builder.fluent.Configurations;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;


import com.infy.UserAuthentication;

public class Tester {
	private static final Log Logger2 = LogFactory.getLog(Tester.class);
	
	public static void main(String[] args) throws Exception{

		Configurations c1 = new Configurations();
		PropertiesConfiguration config = c1.properties("results.properties");

		try {
			UserAuthentication authentication = new UserAuthentication();
			authentication.loginUser("Balaji", "Asdf@123");
			String message = "SUCCESS";
			Logger2.info(config.getProperty(message));
		} catch (Exception exception) {
			if(exception.getMessage().contains("Service.INVALID_CREDENTIALS")) {
				String message = "Service.WRONG_CREDENTIALS";
				Logger2.info(config.getProperty(message));
			}
		}
	}
}
