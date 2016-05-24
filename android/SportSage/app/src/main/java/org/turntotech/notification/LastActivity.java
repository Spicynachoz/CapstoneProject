package org.turntotech.notification;

import android.annotation.TargetApi;
import android.app.Activity;
import android.content.Context;
import android.media.MediaPlayer;
import android.os.Build;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;


public class LastActivity extends Activity {
    List<String[]> list;
    String home;
    String away;
    String percent;
    TextView tv;
    ImageView img_home;
    ImageView img_away;
    int home_id;
    int away_id;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_last);
        tv=(TextView)findViewById(R.id.percent);
        img_home=(ImageView)findViewById(R.id.image_home);
        img_away=(ImageView)findViewById(R.id.image_away);

        String next[] = {};
        list = new ArrayList<String[]>();

        try {
            CSVReader reader = new CSVReader(new InputStreamReader(getAssets().open("best_results.csv")));
            while(true) {
                next = reader.readNext();
                if(next != null) {
                    list.add(next);
                } else {
                    break;
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        findViewById(R.id.match).setOnClickListener(new View.OnClickListener() {
            @TargetApi(Build.VERSION_CODES.JELLY_BEAN)
            public void onClick(View view) {


                home  = String.valueOf(((Spinner) findViewById(R.id.hteam)).getSelectedItem());
                away  = String.valueOf(((Spinner) findViewById(R.id.ateam)).getSelectedItem());


                for (int i = 0; i < list.size(); i++) {

                     //if the input is equal to the matchups from the list
                    if(home.equals(list.get(i)[0]) && away.equals(list.get(i)[1]) ){


                        percent= list.get(i)[2];
                        break;
                    }
                }
                tv.setText(percent + "%");


               home = home.replaceAll(" ", "_").toLowerCase();
               away = away.replaceAll(" ", "_").toLowerCase();


                Context context = img_home.getContext();
                home_id = context.getResources().getIdentifier(home, "drawable", context.getPackageName());
                img_home.setImageResource(home_id);

                Context context2 = img_away.getContext();
                away_id = context2.getResources().getIdentifier(away, "drawable", context2.getPackageName());
                img_away.setImageResource(away_id);

                if ( Integer.valueOf(percent)>50)
                {
                    img_home.setImageAlpha(255);
                    img_away.setImageAlpha(127);
                }
                else if ( Integer.valueOf(percent)<50)
                {
                    img_home.setImageAlpha(127);
                    img_away.setImageAlpha(255);
                }
                else
                {
                    img_home.setImageAlpha(255);
                    img_away.setImageAlpha(255);

                }
            }
        });





    }



}