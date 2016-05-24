package org.turntotech.notification;

import android.app.Activity;
import android.content.Context;
import android.os.Bundle;
import android.view.View;
import android.widget.ListView;
import android.widget.Spinner;
import android.widget.Toast;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class ScheduleChoose extends Activity {
    String month;
    String team;
    Context context= this;
    ArrayList<String[]> list;
    ArrayList<String[]> list_use;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.schedule_choose);
        final ListView lvl = (ListView) findViewById(R.id.ListView00);



        findViewById(R.id.check).setOnClickListener(new View.OnClickListener() {
            public void onClick(View view) {
            list_use=new ArrayList<String[]>();
                String next[] = {};
                list = new ArrayList<String[]>();

                try {
                    CSVReader reader = new CSVReader(new InputStreamReader(getAssets().open("NBASchedule.csv")));
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
                month = String.valueOf(((Spinner) findViewById(R.id.month)).getSelectedItem());
                team = String.valueOf(((Spinner) findViewById(R.id.teams)).getSelectedItem());

                for (int i = 0; i <list.size(); i++) {
                    if ((list.get(i)[0].contains(month.substring(0, 2))) && (((list.get(i)[3]).equals(team)) || ((list.get(i)[5]).equals(team)))) {

                        list_use.add(list.get(i));
                    }
                }

                lvl.setAdapter(new MyCustomBaseAdapter(context, list_use, month, team));
            }

        });


    }
}
