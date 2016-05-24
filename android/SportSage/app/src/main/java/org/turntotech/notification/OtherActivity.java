package org.turntotech.notification;

import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.view.View;


public class OtherActivity extends Activity {
    Intent scheduleIntent;
    Intent aboutIntent;
    Intent lastIntent;

            @Override
            protected void onCreate(Bundle savedInstanceState) {
                scheduleIntent = new Intent(this,ScheduleChoose.class);
                aboutIntent = new Intent(this,AboutUs.class);
                lastIntent =  new Intent(this,LastActivity.class);

                super.onCreate(savedInstanceState);
                setContentView(R.layout.activity_other);

                findViewById(R.id.text1).setOnClickListener(new View.OnClickListener() {
                    public void onClick(View view) {
                        startActivity(scheduleIntent);
                    }
                });


                findViewById(R.id.text2).setOnClickListener(new View.OnClickListener() {
                    public void onClick(View view) {
                        startActivity(aboutIntent);
                    }
                });

                findViewById(R.id.text3).setOnClickListener(new View.OnClickListener() {
                    public void onClick(View view) {
                        startActivity(lastIntent);
                    }
                });

            }


        }