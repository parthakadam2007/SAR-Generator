import { useState } from "react";

export const useManualFetch = <T>(fetcher: () => Promise<T>) => {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(false);

  const execute = async () => {
    setLoading(true);
    const res = await fetcher();
    setData(res);
    setLoading(false);
  };

  return { data, loading, execute };
};
