package org.usfirst.frc.team5482.robot.commands;

import java.net.DatagramSocket;
import java.net.SocketException;

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
    protected void execute() {
    	try {
    		Robot.socket = new DatagramSocket();
    	} catch (SocketException ex){
    		System.out.println("Port occupied.");
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
