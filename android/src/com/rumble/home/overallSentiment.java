package com.rumble.home;

import android.app.Activity;
import android.content.DialogInterface;
import android.content.DialogInterface.OnClickListener;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class overallSentiment extends Activity implements View.OnClickListener{
	
	String EXTRA_MESSAGE = "com.rumble.home.overallSentiment";
	TextView mTextView;
	protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Intent intent = getIntent();
        String message = intent.getStringExtra("text_label");
        
        setContentView(R.layout.overall_sentiment);
        
        mTextView = (TextView) findViewById(R.id.controversyTextView);
        mTextView.setText(message);
        Button topButton =  (Button) findViewById(R.id.topFiveCelebButton); 
        Button negButton =  (Button) findViewById(R.id.negativeButton); 
        Button posButton =  (Button) findViewById(R.id.positiveButton); 
        
        topButton.setOnClickListener((android.view.View.OnClickListener) this);
        negButton.setOnClickListener((android.view.View.OnClickListener) this);
        posButton.setOnClickListener((android.view.View.OnClickListener) this);
	
        
	}
	
	   public void onClick(View v) {
		   String message1;
		   Intent intent;
		   switch(v.getId()) {
	       	   case R.id.topFiveCelebButton:
		       		message1 = "Top 5 Celebrities";   
		       		intent = new Intent(this, ToDoActivity.class);
		    	    intent.putExtra("text_label_2",message1);
		    	    startActivity(intent);
		    	    break;
	       	   case R.id.positiveButton:
		       		message1 = "Positive";   
		       		intent = new Intent(this, ToDoActivity.class);
		    	    intent.putExtra("text_label_2",message1);
		    	    startActivity(intent);
	 	            break;
	           case R.id.negativeButton:
	        	   	message1 = "Negative";   
		       		intent = new Intent(this, ToDoActivity.class);
		    	    intent.putExtra("text_label_2",message1);
		    	    startActivity(intent);
	 	            break;
	           
	       }   
	   }


	   }		


