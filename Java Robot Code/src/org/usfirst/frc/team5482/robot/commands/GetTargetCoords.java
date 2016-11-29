package org.usfirst.frc.team5482.robot.commands;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.net.UnknownHostException;

import org.usfirst.frc.team5482.robot.Constants;
import org.usfirst.frc.team5482.robot.Robot;

import edu.wpi.first.wpilibj.command.Command;

/**
 *
 */
public class GetTargetCoords extends Command {

	public GetTargetCoords() {
		// Use requires() here to declare subsystem dependencies
		// eg. requires(chassis);
	}

	// Called just before this Command runs the first time
	protected void initialize() {

	}

	// Called repeatedly when this Command is scheduled to run
	protected void execute(){
		try {
			Robot.socket = new DatagramSocket();
			byte[] receiveData = new byte[1024];
			byte[] sendData = new byte[1024];

			while (true /* change this to stop later */) {
				
				String request = "gib datas";
				
				sendData = request.getBytes();
				
				DatagramPacket sendPacket =
						new DatagramPacket(sendData, sendData.length, InetAddress.getByName(Constants.piAddress), Constants.piPort);
				
				Robot.socket.send(sendPacket);
				
				receiveData = new byte[1024];

				DatagramPacket receivePacket = 
						new DatagramPacket(receiveData, receiveData.length);
				
				System.out.println("Waiting for packet...");
				
				try {
					Robot.socket.receive(receivePacket);
				} catch (IOException e) {
					System.out.println("Error!\n" + e);
				}
				
				String data = new String(receivePacket.getData());
				
				InetAddress IPAddress = receivePacket.getAddress();
				
				int port = receivePacket.getPort();
				
				System.out.println("From: " + IPAddress + ":" + port);
				System.out.println("Message: " + data);
			}
		} catch (SocketException ex) {
			System.out.println("Port occupied.");
		} catch (UnknownHostException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		} catch (IOException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
	}

	// Make this return true when this Command no longer needs to run execute()
	protected boolean isFinished() {
		return false;
	}

	// Called once after isFinished returns true
	protected void end() {
	}

	// Called when another command which requires one or more of the same
	// subsystems is scheduled to run
	protected void interrupted() {
	}
}
