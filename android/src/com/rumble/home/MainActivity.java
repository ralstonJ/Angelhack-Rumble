package com.rumble.home;

import java.net.MalformedURLException;

import com.microsoft.windowsazure.mobileservices.MobileServiceClient;

import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.view.KeyEvent;
import android.view.Menu;
import android.view.View;
import android.view.inputmethod.EditorInfo;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.TextView.OnEditorActionListener;
import com.microsoft.windowsazure.mobileservices.*;

public class MainActivity extends Activity {
	public final static String EXTRA_MESSAGE = "com.example..MESSAGE";
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		
		final EditText editText = (EditText) findViewById(R.id.searchEditText);
		
		
		editText.setOnEditorActionListener(new OnEditorActionListener() {

			// search listener
			@Override
			public boolean onEditorAction(TextView arg0, int arg1, KeyEvent arg2) {
				 boolean handled = false;
				 if(arg1 == EditorInfo.IME_ACTION_SEARCH){
					 sendMessage(editText.getText().toString());
					 handled =true;
				 }
				return handled;
			}
			
		});
		
	}
	public void sendMessage(String message) {
		
	    Intent intent = new Intent(this, overallSentiment.class);
	    intent.putExtra("text_label",message);
	    startActivity(intent);
	}
	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.activity_main, menu);
		return true;
	}

	public class Item {
	    public int Id;
	    public String Text;
	}
}
