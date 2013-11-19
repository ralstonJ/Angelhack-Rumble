package com.rumble.home;

// TODO uncomment these lines when using Mobile Services
//import com.microsoft.windowsazure.mobileservices.MobileServiceClient;
//import com.microsoft.windowsazure.mobileservices.MobileServiceTable;
//import com.microsoft.windowsazure.mobileservices.NextServiceFilterCallback;
//import com.microsoft.windowsazure.mobileservices.ServiceFilter;
//import com.microsoft.windowsazure.mobileservices.ServiceFilterRequest;
//import com.microsoft.windowsazure.mobileservices.ServiceFilterResponse;
//import com.microsoft.windowsazure.mobileservices.ServiceFilterResponseCallback;
//import com.microsoft.windowsazure.mobileservices.TableOperationCallback;
//import com.microsoft.windowsazure.mobileservices.TableQueryCallback;
//
//import java.net.MalformedURLException;


import java.util.List;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.ProgressBar;
import android.widget.TextView;

import com.rumble.home.R;
import com.microsoft.windowsazure.mobileservices.MobileServiceClient;
import com.microsoft.windowsazure.mobileservices.MobileServiceTable;
import com.microsoft.windowsazure.mobileservices.NextServiceFilterCallback;
import com.microsoft.windowsazure.mobileservices.ServiceFilter;
import com.microsoft.windowsazure.mobileservices.ServiceFilterRequest;
import com.microsoft.windowsazure.mobileservices.ServiceFilterResponse;
import com.microsoft.windowsazure.mobileservices.ServiceFilterResponseCallback;
import com.microsoft.windowsazure.mobileservices.TableOperationCallback;
import com.microsoft.windowsazure.mobileservices.TableQueryCallback;


import java.net.MalformedURLException;
public class ToDoActivity extends Activity {
	TextView titleTextView;
	//	TODO Uncomment these lines to create references to the mobile service client and table
	private MobileServiceClient mClient;
	private MobileServiceTable<ToDoItem> mToDoTable;

//  TODO Comment out this line to remove the in-memory store
	
	private ToDoItemAdapter mAdapter;
	private EditText mTextNewToDo;
	private ProgressBar mProgressBar;
	
	/**
	 * Initializes the activity
	 */
	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_to_do);
		Intent intent = getIntent();
        String message = intent.getStringExtra("text_label_2");
		
		titleTextView =(TextView) findViewById(R.id.textViewTitle);
		mProgressBar = (ProgressBar) findViewById(R.id.loadingProgressBar);
		titleTextView.setText(message);	
		// Initialize the progress bar
		mProgressBar.setVisibility(ProgressBar.GONE);

//		TODO Uncomment the the following code to create the mobile services client
		try {
//			// Create the Mobile Service Client instance, using the provided
//			// Mobile Service URL and key
			mClient = new MobileServiceClient(
					"https://rumblemsurl.azure-mobile.net/",
					"VCwmuQxSlOMMMaXdiVgkKDkEYlBBxo58", 
					this).withFilter(new ProgressFilter());

//			// Get the Mobile Service Table instance to use
			mToDoTable = mClient.getTable(ToDoItem.class);
		} catch (MalformedURLException e) {
			createAndShowDialog(new Exception("There was an error creating the Mobile Service. Verify the URL"), "Error");
		}
		
//1		mTextNewToDo = (EditText) findViewById(R.id.textNewToDo);

		// Create an adapter to bind the items with the view
		mAdapter = new ToDoItemAdapter(this, R.layout.row_list_to_do);
		ListView listViewToDo = (ListView) findViewById(R.id.listViewToDo);
		listViewToDo.setAdapter(mAdapter);
	
		// Load the items from the Mobile Service
		refreshItemsFromTable();
		
	}
	
	/**
	 * Initializes the activity menu
	 */
	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		getMenuInflater().inflate(R.menu.activity_main, menu);
		return true;
	}
	
	/**
	 * Select an option from the menu
	 */
	@Override
	public boolean onOptionsItemSelected(MenuItem item) {
		if (item.getItemId() == R.id.menu_refresh) {
			refreshItemsFromTable();
		}
		
		return true;
	}

	/**
	 * Mark an item as completed
	 * 
	 * @param item
	 *            The item to mark
	 */
	public void checkItem(ToDoItem item) {
		
		// Set the item as completed and update it in the table
		item.setComplete(true);

//		TODO Uncomment the the following code when using a mobile service
		mToDoTable.update(item, new TableOperationCallback<ToDoItem>() {
			public void onCompleted(ToDoItem entity, Exception exception, ServiceFilterResponse response) {
				if (exception == null) {
					if (entity.isComplete()) {
						mAdapter.remove(entity);
					}
				} else {
					createAndShowDialog(exception, "Error");
				}
			}
		});

//		TODO Comment out these lines to remove the in-memory store
		if (item.isComplete()) {
			mAdapter.remove(item);
		}
//		End of lines to comment out
		
	}

	/**
	 * Add a new item
	 * 
	 * @param view
	 *            The view that originated the call
	 */
	public void addItem(View view) {
		
		// Create a new item
		ToDoItem item = new ToDoItem();

		item.setText(mTextNewToDo.getText().toString());
		item.setComplete(false);
		
//		TODO Uncomment the the following code when using a mobile service
//		// Insert the new item
		mToDoTable.insert(item, new TableOperationCallback<ToDoItem>() {
//
			public void onCompleted(ToDoItem entity, Exception exception, ServiceFilterResponse response) {
//				
				if (exception == null) {
					if (!entity.isComplete()) {
						mAdapter.add(entity);
					}
				} else {
					createAndShowDialog(exception, "Error");
				}

			}
		});

//	    TODO Comment out these lines to remove the in-memory store
		mAdapter.add(item);
//		End of lines to comment out
		
		mTextNewToDo.setText("");
	}

	/** 
	 * Refresh the list with the items in the Mobile Service Table
	 */
	private void refreshItemsFromTable() {

//		TODO Uncomment the the following code when using a mobile service
//		// Get the items that weren't marked as completed and add them in the adapter
		mToDoTable.where().field("complete").eq(false).execute(new TableQueryCallback<ToDoItem>() {
//
			public void onCompleted(List<ToDoItem> result, int count, Exception exception, ServiceFilterResponse response) {
				if (exception == null) {
					mAdapter.clear();
//
					for (ToDoItem item : result) {
						mAdapter.add(item);
					}

				} else {
					createAndShowDialog(exception, "Error");
				}
			}
		});
		
//		TODO Comment out these lines to remove the in-memory store	
		mAdapter.clear();
//		End of lines to comment out

		
		
	}

	/**
	 * Creates a dialog and shows it
	 * 
	 * @param exception
	 *            The exception to show in the dialog
	 * @param title
	 *            The dialog title
	 */
	private void createAndShowDialog(Exception exception, String title) {
		createAndShowDialog(exception.toString(), title);
	}

	/**
	 * Creates a dialog and shows it
	 * 
	 * @param message
	 *            The dialog message
	 * @param title
	 *            The dialog title
	 */
	private void createAndShowDialog(String message, String title) {
		AlertDialog.Builder builder = new AlertDialog.Builder(this);

		builder.setMessage(message);
		builder.setTitle(title);
		builder.create().show();
	}
	

//	TODO Uncomment the the following code when using a mobile service
	private class ProgressFilter implements ServiceFilter {
//		
//		@Override
		public void handleRequest(ServiceFilterRequest request, NextServiceFilterCallback nextServiceFilterCallback,
				final ServiceFilterResponseCallback responseCallback) {
			runOnUiThread(new Runnable() {
//
//				@Override
				public void run() {
					mProgressBar.setVisibility(ProgressBar.VISIBLE);
				}
			});
//			
			nextServiceFilterCallback.onNext(request, new ServiceFilterResponseCallback() {
//				
//				@Override
				public void onResponse(ServiceFilterResponse response, Exception exception) {
					runOnUiThread(new Runnable() {
//
//						@Override
						public void run() {
							mProgressBar.setVisibility(ProgressBar.GONE);
						}
					});
//					
					responseCallback.onResponse(response, exception);
				}
			});
		}
	}
}
