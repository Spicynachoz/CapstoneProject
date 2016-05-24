
package org.turntotech.notification;

import android.annotation.TargetApi;
import android.graphics.Color;
import android.graphics.drawable.ColorDrawable;
import android.media.MediaPlayer;
import android.os.Build;
import android.os.Bundle;
import android.app.Activity;
import android.app.Notification;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.os.CountDownTimer;
import android.os.Handler;
import android.text.format.DateFormat;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;


public class MainActivity extends Activity {
    Intent otherIntent;
	//delay in ms
	int DELAY = 3000;
	private ImageView image;


	@Override
	protected void onCreate(Bundle savedInstanceState) {


		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
        Log.i("TurnToTech", "Project Name - Notification");

		otherIntent=new Intent(this, OtherActivity.class);
        image= (ImageView)findViewById(R.id.text6);
		Handler handler = new Handler();
		handler.postDelayed(new Runnable() {


			@Override
			public void run(){


				startActivity(otherIntent);
			}
		}, DELAY);


		image.setOnTouchListener(new OnSwipeTouchListener(MainActivity.this) {
			@Override
			public void onSwipeLeft() {
				startActivity(otherIntent);

			}

		});

	}

	}








