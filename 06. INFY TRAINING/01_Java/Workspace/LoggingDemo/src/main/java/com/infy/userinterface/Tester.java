package com.infy.userinterface;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import com.infy.UserAuthentication;

public class Tester {
	private static final Log Logger2 = LogFactory.getLog(Tester.class);

	public static void main(String[] args) {
		try {
			UserAuthentication authentication = new UserAuthentication();
			authentication.loginUser("Balaji", "Asdf@123");
			Logger2.info("User has logged in successfully");
		} catch (Exception exception) {
			Logger2.info(exception.getMessage());
		}
	}
}
